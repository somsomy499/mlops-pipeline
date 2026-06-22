from mlops_pipeline import Pipeline

def test_pipeline_stages():
    p = Pipeline("test")
    assert p.stages == []
