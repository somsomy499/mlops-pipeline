"""Model monitoring and drift detection."""
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from collections import deque

@dataclass
class DriftAlert:
    metric_name: str
    current_value: float
    baseline_value: float
    drift_score: float
    severity: str  # low, medium, high
    timestamp: float = field(default_factory=time.time)

class ModelMonitor:
    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self.baselines: Dict[str, float] = {}
        self.windows: Dict[str, deque] = {}
        self.alerts: List[DriftAlert] = []
        
    def set_baseline(self, metric: str, value: float):
        self.baselines[metric] = value
        self.windows[metric] = deque(maxlen=self.window_size)
        
    def record(self, metric: str, value: float):
        if metric not in self.windows:
            self.windows[metric] = deque(maxlen=self.window_size)
        self.windows[metric].append(value)
        
        if metric in self.baselines:
            drift = self._detect_drift(metric, value)
            if drift:
                self.alerts.append(drift)
                
    def _detect_drift(self, metric, current):
        baseline = self.baselines[metric]
        if baseline == 0:
            return None
        drift_score = abs(current - baseline) / abs(baseline)
        if drift_score > 0.1:
            severity = "high" if drift_score > 0.25 else "medium" if drift_score > 0.15 else "low"
            return DriftAlert(metric, current, baseline, drift_score, severity)
        return None
        
    def get_metrics(self, metric: str):
        window = self.windows.get(metric, deque())
        if not window:
            return {}
        values = list(window)
        return {
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
            "count": len(values),
        }
