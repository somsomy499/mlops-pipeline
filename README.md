# MLOps Pipeline 🔄

End-to-end MLOps pipeline with data validation, training, evaluation, and deployment.

## Features

- **Data Validation**: Great Expectations integration
- **Training**: Multi-GPU, distributed training support
- **Evaluation**: Automated model comparison
- **Deployment**: Docker + Kubernetes ready
- **MLflow Integration**: Experiment tracking, model registry
- **CI/CD**: GitHub Actions templates

## Quick Start

```python
from mlops_pipeline import Pipeline

pipeline = Pipeline(experiment_name="my-model")
pipeline.validate_data(train_df, schema=data_schema)
pipeline.train(model, train_df, val_df, params={"epochs": 10})
pipeline.evaluate(test_df, metrics=["accuracy", "f1"])
pipeline.deploy(target="kubernetes", replicas=3)
```

## License

MIT