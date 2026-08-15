# 🌿 Plant Disease Detection

Production-grade plant disease detection for **potato, tomato and pepper** crops (15 classes) — a
training pipeline orchestrated by DVC (data versioning only) with MLflow as the single source of
truth for experiments and model versions, a FastAPI serving layer with a Groq-powered RAG chatbot, and a
Streamlit frontend.

**Division of responsibility:** DVC versions data (`data/raw/images`, `data/processed/*`) and
orchestrates the `prepare → train → evaluate` pipeline (knows what needs to re-run). MLflow tracks
everything about experiments and models — hyperparameters, per-epoch metrics, evaluation results,
and versioned model artifacts via its Model Registry. Neither system duplicates the other's job.

---

## Project Structure

```
plant-disease-detection/
├── README.md
├── requirements.txt              # pinned production (serving) deps
├── requirements-train.txt         # + training-only deps (matplotlib, scikit-learn, dvc)
├── setup.py                        # setuptools shim — metadata lives in pyproject.toml
├── pyproject.toml                   # package config + dev/train extras
├── params.yaml                       # DVC-tracked hyperparameters (dvc.yaml stages reference this)
├── dvc.yaml                           # pipeline: prepare -> train -> evaluate
├── .env.example                        # environment variable template
├── Makefile                             # developer shortcuts
├── Dockerfile                             # backend: multi-stage, non-root, python:3.10-slim
├── docker-compose.yml                      # api + mlflow + frontend services
│
├── config/
│   └── config.yaml               # canonical 15-class list — single source of truth for
│                                   # both training (label order) and serving (display names)
│
├── data/                          # DVC-tracked, not committed to git — see "Dataset" below
│   ├── raw/
│   │   └── images/                #   data/raw/images.dvc tracks this — one folder per class
│   │       ├── Pepper__bell___Bacterial_spot/
│   │       ├── Potato___Early_blight/
│   │       └── ...
│   ├── processed/                 #   `prepare` stage output — materialized splits (hardlinks
│   │   ├── train/                 #   back to data/raw, so this costs zero extra disk)
│   │   ├── val/
│   │   └── test/
│   └── external/                  #   placeholder for any externally-sourced auxiliary data
│
├── notebooks/                     # exploratory notebooks (empty by default, .gitkeep only)
│
├── src/
│   ├── data/
│   │   ├── make_dataset.py       # DVC "prepare" stage: raw -> processed train/val/test split
│   │   └── preprocess.py          # dataset loading + augmentation layers
│   ├── models/
│   │   ├── model.py               # CNN architecture
│   │   ├── train.py                # DVC "train" stage: trains, checkpoints, logs to MLflow
│   │   └── evaluate.py              # DVC "evaluate" stage: confusion matrix, curves, report
│   ├── utils/
│   │   └── common.py                # config.yaml / params.yaml loaders, logger
│   └── plant_api/                     # SERVING package (FastAPI)
│       ├── main.py                     #   app factory
│       ├── config.py                    #   Pydantic Settings (reads config/config.yaml)
│       ├── dependencies.py               #   dependency injection
│       ├── routers/                       #   health | predict | chat
│       ├── services/                       #   ModelService | MlflowService | ChatService
│       ├── schemas/                         #   Pydantic request/response models
│       └── knowledge/                        #   disease knowledge base (RAG), all 15 classes
│
├── tests/                         # pytest suite (mocked services)
│
├── models/                        # local copy of the model the API loads — gitignored, versioned
│   ├── plant_disease_model.keras  #   by MLflow's Model Registry, NOT DVC (dvc.yaml outs are
│   └── checkpoints/                #   cache:false — DVC orchestrates but doesn't own/cache them)
│       └── best.keras
│
├── logs/
│   └── training/<run_id>/          # TensorBoard logs per training run
│
├── reports/                       # local copies of what's ALSO logged to MLflow — regenerable,
│   ├── metrics.json                # gitignored, not DVC-cached
│   ├── training_history.json
│   ├── evaluation.txt
│   └── figures/                     # confusion_matrix.png, training_curve.png, sample_predictions.png
│
├── scripts/                       # thin CLI wrappers around src/
│   ├── make_dataset.py
│   ├── train.py
│   ├── evaluate.py
│   └── convert_model.py           # Keras → TFLite converter
│
├── app/
│   ├── app.py                     # launches backend (uvicorn) + frontend (streamlit) together
│   ├── streamlit_app.py            # upload leaf → prediction + chart + disease info + chat
│   ├── templates/                   # reserved for future server-rendered pages (Jinja2)
│   ├── requirements.txt              # frontend-only deps (streamlit, requests)
│   └── Dockerfile                     # lightweight image, no TensorFlow/MLflow
│
└── .github/workflows/ci-cd.yml    # lint → test → docker push
```

> **Dependency isolation:** the backend/training venv and the frontend (Streamlit) venv must stay
> separate — `streamlit` pulls in a `protobuf`/`starlette` chain that conflicts with
> TensorFlow/FastAPI/MLflow's pinned versions. Install `app/requirements.txt` in its own
> environment (or just use the Docker `frontend` service) — never into the venv you run
> `scripts/train.py` or the API from.

---

## Detected Classes (15)

| Crop | Classes |
|------|---------|
| 🫑 Pepper | Bacterial Spot · Healthy |
| 🥔 Potato | Early Blight · Late Blight · Healthy |
| 🍅 Tomato | Bacterial Spot · Early Blight · Late Blight · Leaf Mold · Septoria Leaf Spot · Spider Mites · Target Spot · Yellow Leaf Curl Virus · Mosaic Virus · Healthy |

Full disease info (symptoms, causes, treatment, prevention, pesticides) lives in
`src/plant_api/knowledge/knowledge_base.py` and backs the `/predict` response and the `/chat` RAG
context.

---

## Dataset & DVC

Raw images live in `data/raw/images/<class>/*.jpg` (the standard
[PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease) layout) and are tracked by DVC,
not git — `data/raw/images.dvc` holds the hash, `data/raw/.gitignore` (auto-generated by `dvc add`)
keeps the actual files out of git.

```bash
make install-train        # pulls in dvc + training deps
dvc pull                  # fetch data/raw/images from your configured DVC remote
                           # (no remote configured yet — see below)
```

**No remote is configured yet.** `dvc add`/pipeline caching works locally (`.dvc/cache`) without
one, but `dvc push`/`dvc pull` need a remote to share data across machines:

```bash
dvc remote add -d storage <s3://... | gs://... | /local/path | ...>
dvc push
```

Class folder names **must** match `config/config.yaml` — both `make_dataset.py` and `train.py`
validate this and fail fast with a clear diff on mismatch, since a silent mismatch would mean the
API mis-labels predictions.

### The pipeline (`dvc.yaml`)

```
prepare  →  train  →  evaluate
```

DVC orchestrates all three stages (knows what needs to re-run based on changed deps/params) but only
*caches/versions* `prepare`'s output — `data/processed/*` is real data. `train`'s and `evaluate`'s
outputs are declared `cache: false`: DVC still tracks them for pipeline freshness, but ownership of
versioning stops there — that's MLflow's job.

- **prepare** (`src/data/make_dataset.py`): splits `data/raw/images` into
  `data/processed/{train,val,test}` per `params.yaml`'s `prepare.*` ratios. Uses **hardlinks**, not
  copies — same files, zero extra disk.
- **train** (`src/models/train.py`): builds the CNN, trains with `EarlyStopping` +
  `ModelCheckpoint`, logs params/per-epoch metrics/TensorBoard to MLflow, saves
  `models/plant_disease_model.keras` locally (what the API loads) **and** logs + registers it as a
  new version in MLflow's Model Registry (`mlflow.keras.log_model(..., registered_model_name=...)`).
  Writes its MLflow run ID to `models/.mlflow_run_id` (gitignored) so `evaluate` can resume it.
- **evaluate** (`src/models/evaluate.py`): scores the held-out test split, writes local report files
  under `reports/`, and — if `models/.mlflow_run_id` exists — resumes that **same** MLflow run to
  attach eval metrics (accuracy, macro/weighted precision/recall/F1) and the figures as artifacts.
  Net result: one MLflow run per training pipeline execution holds hyperparameters, training curves,
  the registered model, and evaluation results together.

Run it:

```bash
dvc repro                 # full pipeline, only re-runs stages whose deps/params changed
dvc repro train           # just one stage
```

Or run stages directly without DVC's caching/skip logic:

```bash
make prepare-data
make train                # or: make train-smoke (2 epochs, quick sanity check)
make evaluate
make convert-model        # Keras → TFLite, for the API/mobile
```

**Architecture note:** the CNN uses six 3×3 valid-padding Conv+MaxPool blocks, which requires the
default 256×256 input — a much smaller `image_size` in `params.yaml` will collapse the spatial
dimensions to zero/negative by the final conv layer and fail.

To change hyperparameters, edit `params.yaml` (not the scripts) — that's what keeps `dvc repro`
reproducible and diffable.

---

## Serving — Quick Start

### 1. Install

```bash
cp .env.example .env          # add your GROQ_API_KEY (free tier: console.groq.com)
pip install -e ".[dev]"
```

### 2. Run locally

```bash
make run
# API docs: http://localhost:8000/docs
```

### 3. Run everything (API + Streamlit) with Docker

```bash
make docker-up
# API:      http://localhost:8000/docs
# Frontend: http://localhost:8501
# MLflow:   http://localhost:5000
```

### 4. Run API + Streamlit locally without Docker

```bash
python app/app.py
# assumes the current interpreter has no dependency conflict; for a genuinely
# separate frontend venv: FRONTEND_PYTHON=/path/to/venv/bin/python python app/app.py
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | API info |
| `GET` | `/health` | Health + model status |
| `POST` | `/predict` | Upload a plant leaf image (potato, tomato or pepper) → disease prediction |
| `POST` | `/chat` | Chat with a Groq-hosted LLM about plant diseases |

---

## MLflow Tracking

MLflow is the single source of truth for experiments and model versions — training, evaluation, and
serving all point at the **same** server by default (`http://localhost:5000`, i.e. `docker compose
up`'s `mlflow` service), so everything shows up together instead of scattered across a local
`mlruns/` folder and a server. Override with the `MLFLOW_TRACKING_URI` env var if that URL doesn't
resolve in your setup; if the server isn't reachable, tracking is disabled with a warning rather than
failing the run.

Two experiments:
- **`plant-disease-training`** — one run per training pipeline execution: hyperparameters, per-epoch
  accuracy/loss, final test accuracy, evaluation metrics (`eval_accuracy`,
  `eval_macro_avg_f1_score`, etc.), and artifacts (the registered model, `training_history.json`,
  `evaluation.txt`, confusion matrix / sample predictions / training curve figures) — all in one run.
- **`plant-disease-detection`** — one run per `/predict` request: predicted class, confidence, and
  per-class probabilities.

**Model versions:** every successful training run registers a new version of `plant_disease_model`
under MLflow's Model Registry (Models tab) — v1, v2, v3... each pointing at the exact run that
produced it, so you can trace any served model back to its hyperparameters and metrics.

```bash
make mlflow-ui   # → http://localhost:5000 (standalone; use this OR docker compose's mlflow service)
```

> **Windows note:** MLflow prints emoji ("🏃 View run...") on successful completion, which crashes on
> Windows' default console codepage. `scripts/train.py`/`scripts/evaluate.py` reconfigure
> stdout/stderr to UTF-8 on `win32` to avoid this — if you invoke `src.models.train.run()` some other
> way on Windows, do the same.

---

## CI/CD Pipeline

```
Push to main / PR
    │
    ├── 1. lint    → ruff check + format check (src/, tests/, scripts/, app/)
    ├── 2. test    → pytest + coverage report
    └── 3. docker  → build & push to Docker Hub (main only)
```

Training is not part of CI — it needs the dataset (`dvc pull`) and meaningful CPU/GPU time; CI only
tests and ships the serving API against whatever model is already in `models/`.

**Required GitHub Secrets:**
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `GROQ_API_KEY`

---

## Development Commands

```bash
make install          # install production dependencies
make install-dev        # install dependencies + dev tools
make install-train        # install dependencies + training tools (dvc, matplotlib, scikit-learn)
make test                   # run test suite
make lint                     # ruff linter
make format                     # ruff auto-format
make prepare-data                  # DVC "prepare" stage
make train                            # DVC "train" stage (or make train-smoke)
make evaluate                            # DVC "evaluate" stage
make convert-model                          # Keras → TFLite
make dvc-repro                                 # full pipeline via DVC
make frontend                                     # Streamlit only (needs its own venv)
make app                                             # backend + frontend together
make docker-up                                          # full stack via Docker
make mlflow-ui                                             # open MLflow dashboard
make clean                                                    # remove caches
```
