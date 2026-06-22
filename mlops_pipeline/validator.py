"""Data validation pipeline."""
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

@dataclass
class ValidationRule:
    name: str
    field: str
    rule_type: str  # not_null, range, regex, unique
    params: Dict[str, Any] = None

@dataclass  
class ValidationResult:
    rule: str
    passed: bool
    errors: List[str]
    rows_checked: int

class DataValidator:
    def __init__(self, rules: List[ValidationRule] = None):
        self.rules = rules or []
        self.results = []
        
    def add_rule(self, rule: ValidationRule):
        self.rules.append(rule)
        
    def validate(self, data: List[Dict]) -> List[ValidationResult]:
        self.results = []
        for rule in self.rules:
            result = self._apply_rule(rule, data)
            self.results.append(result)
        return self.results
        
    def _apply_rule(self, rule, data):
        errors = []
        for row in data:
            val = row.get(rule.field)
            if rule.rule_type == "not_null" and val is None:
                errors.append(f"Row {row.get("id", "?")}: {rule.field} is null")
            elif rule.rule_type == "range":
                if val is not None:
                    min_val = rule.params.get("min", float("-inf"))
                    max_val = rule.params.get("max", float("inf"))
                    if not (min_val <= val <= max_val):
                        errors.append(f"Row {row.get("id", "?")}: {rule.field}={val} out of range")
        return ValidationResult(
            rule=rule.name, passed=len(errors) == 0,
            errors=errors, rows_checked=len(data)
        )
        
    def summary(self):
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        return {"total": total, "passed": passed, "failed": total - passed}
