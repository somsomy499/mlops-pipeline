# Monitoring Guide

## Metrics to Track

| Metric | Baseline | Alert Threshold |
|--------|----------|----------------|
| Prediction latency | 100ms | >200ms |
| Error rate | 0.1% | >1% |
| Data drift (PSI) | 0.0 | >0.1 |
| Model accuracy | 0.90 | <0.85 |

## Alert Severity

- **Low**: Drift 10-15% — informational
- **Medium**: Drift 15-25% — investigate
- **High**: Drift >25% — retrain model
