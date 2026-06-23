# MLOps Pipeline

End-to-end MLOps pipeline with experiment tracking, data versioning, and model deployment.

## Components
- **MLflow** — Experiment tracking & model registry
- **DVC** — Data versioning
- **Docker** — Model serving container
- **FastAPI** — Inference API

## Quick Start
```bash
dvc pull
python train.py  # Logs to MLflow
dvc push
docker build -t ml-model .
```

## License
MIT