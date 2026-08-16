# ============================================================
# Stage 1: Builder — install Python dependencies
# ============================================================
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ============================================================
# Stage 2: Runtime — slim production image
# ============================================================
FROM python:3.11-slim AS runtime

# Security: run as non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application source and package config
COPY src/ ./src/
COPY config/ ./config/
COPY pyproject.toml .
COPY setup.py .

# Install the package itself (deps already present)
RUN pip install --no-cache-dir --no-deps -e .

# Copy model files
COPY models/ ./models/

# MLflow artifact directory
RUN mkdir -p /app/mlruns && chown -R appuser:appuser /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MODEL_DIR=/app/models \
    MLFLOW_TRACKING_URI=/app/mlruns

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "src.plant_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
