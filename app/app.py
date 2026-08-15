"""Launches the FastAPI backend and the Streamlit frontend together for local dev/demo.

The two have deliberately separate dependency sets (see app/requirements.txt vs.
requirements.txt — streamlit's dependency chain conflicts with FastAPI/TensorFlow/
MLflow's pinned versions), so this script starts each as its own subprocess and
lets you point it at a different Python interpreter per side:

    python app/app.py
    FRONTEND_PYTHON=/path/to/frontend-venv/bin/python python app/app.py

If FRONTEND_PYTHON is not set, it falls back to the current interpreter — fine
only if you've verified there's no dependency conflict in that environment.
"""

import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_PORT = os.environ.get("BACKEND_PORT", "8000")
FRONTEND_PORT = os.environ.get("FRONTEND_PORT", "8501")
FRONTEND_PYTHON = os.environ.get("FRONTEND_PYTHON", sys.executable)


def main() -> None:
    backend = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "src.plant_api.main:app",
            "--host",
            "0.0.0.0",
            "--port",
            BACKEND_PORT,
        ],
        cwd=REPO_ROOT,
    )

    frontend_env = {**os.environ, "API_URL": f"http://localhost:{BACKEND_PORT}"}
    frontend = subprocess.Popen(
        [
            FRONTEND_PYTHON,
            "-m",
            "streamlit",
            "run",
            os.path.join(REPO_ROOT, "app", "streamlit_app.py"),
            "--server.port",
            FRONTEND_PORT,
        ],
        cwd=REPO_ROOT,
        env=frontend_env,
    )

    print(f"\nBackend:  http://localhost:{BACKEND_PORT}/docs")
    print(f"Frontend: http://localhost:{FRONTEND_PORT}\n")

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        backend.terminate()
        frontend.terminate()


if __name__ == "__main__":
    main()
