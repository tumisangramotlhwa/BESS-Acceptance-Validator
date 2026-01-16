from typing import Dict, Any
import pandas as pd
from .checks import check_std, check_bounds, check_ramp_rate


def evaluate(df: pd.DataFrame, criteria: Dict[str, Any]) -> list[dict]:

    results = []

    dt_s = df["timestamp"].diff().dt.total_seconds().median()

    for test in criteria["tests"]:
        signal = df[test["signal"]]

        if "max_std" in test:
            passed = check_std(signal, test["max_std"])

        elif "min" in test and "max" in test:
            passed = check_bounds(signal, test["min"], test["max"])

        elif "max_delta_per_s" in test:
            passed = check_ramp_rate(signal, test["max_delta_per_s"], dt_s)

        else:
            passed = False

        results.append({
            "name": test["name"],
            "signal": test["signal"],
            "passed": passed
        })

    return results
