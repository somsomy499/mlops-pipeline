from mlops_pipeline.validator import DataValidator, ValidationRule

def test_not_null_rule():
    v = DataValidator([ValidationRule("check_name", "name", "not_null")])
    result = v.validate([{"id": 1, "name": "Alice"}, {"id": 2, "name": None}])
    assert not result[0].passed
    assert len(result[0].errors) == 1

def test_range_rule():
    v = DataValidator([ValidationRule("check_age", "age", "range", {"min": 0, "max": 150})])
    result = v.validate([{"id": 1, "age": 25}, {"id": 2, "age": 200}])
    assert result[0].passed
    assert not result[0].passed  # age 200 fails
