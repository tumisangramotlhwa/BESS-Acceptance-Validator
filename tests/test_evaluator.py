import pandas as pd
from validator.evaluator import evaluate


def test_evaluate_mixed_results():
    df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=3, freq="s"),
        "power_kw": [100, 101, 300],
        "frequency_hz": [50.0, 50.1, 50.0],
    })

    criteria = {
        "tests": [
            {
                "name": "freq_ok",
                "signal": "frequency_hz",
                "min": 49.8,
                "max": 50.2
            },
            {
                "name": "ramp_fail",
                "signal": "power_kw",
                "max_delta_per_s": 50
            }
        ]
    }

    results = evaluate(df, criteria)

    assert results[0]["passed"] is True
    assert results[1]["passed"] is False
