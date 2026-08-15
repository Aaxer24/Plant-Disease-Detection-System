.PHONY: install install-dev install-train lint format test run \
        prepare-data train train-smoke evaluate convert-model dvc-repro \
        frontend app docker-build docker-up docker-down mlflow-ui clean

# NOTE: activate the venv first (e.g. `conda activate ./venv` on Windows) —
# every target below assumes "python"/"pip"/"dvc"/etc. resolve to it via PATH.
# Do not hardcode venv paths here: forward-slash paths like "venv/python.exe"
# fail under native cmd.exe (works fine from bash, breaks from a plain Windows
# terminal) — bare commands + an activated env is the only combination that
# works consistently across shells.

# ── Setup ────────────────────────────────────────────────────────────────────
install:
	pip install -r requirements.txt && pip install --no-deps -e .

install-dev:
	pip install -r requirements.txt && pip install -e ".[dev]"

install-train:
	pip install -r requirements-train.txt && pip install --no-deps -e ".[train]"

# ── Code Quality ─────────────────────────────────────────────────────────────
lint:
	ruff check src/ tests/ scripts/ app/

format:
	ruff format src/ tests/ scripts/ app/

# ── Testing ──────────────────────────────────────────────────────────────────
test:
	pytest tests/ -v --cov=src.plant_api --cov-report=term-missing

# ── Run locally (API only) ──────────────────────────────────────────────────
run:
	uvicorn src.plant_api.main:app --reload --host 0.0.0.0 --port 8000

# ── Training pipeline (DVC-tracked — see dvc.yaml, params.yaml) ────────────
# Run ONE of these at a time — never `dvc repro` from two shells simultaneously,
# it will clear a stage's outputs mid-run out from under the other process.
prepare-data:
	python scripts/make_dataset.py

train:
	python scripts/train.py

train-smoke:
	python scripts/train.py --epochs 2

evaluate:
	python scripts/evaluate.py

convert-model:
	python scripts/convert_model.py

dvc-repro:
	dvc repro

# ── Frontend (deliberately a SEPARATE environment — see README) ────────────
frontend:
	streamlit run app/streamlit_app.py

app:
	python app/app.py

# ── Docker ───────────────────────────────────────────────────────────────────
docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

# ── MLflow UI ────────────────────────────────────────────────────────────────
mlflow-ui:
	mlflow ui --port 5000 --backend-store-uri mlruns

# ── Cleanup ───────────────────────────────────────────────────────────────────
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache htmlcov .coverage coverage.xml mlruns
