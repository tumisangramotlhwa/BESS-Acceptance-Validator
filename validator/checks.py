import pandas as pd
import numpy as np

def check_std(signal: pd.Series, max_std: float) -> bool:
    return signal.std() <= max_std


def check_bounds(signal: pd.Series, min_val: float, max_val: float) -> bool:
    return signal.between(min_val, max_val).all()


def check_ramp_rate(signal: pd.Series, max_delta_per_s: float, dt_s: float) -> bool:
    deltas = signal.diff().abs() / dt_s
    return deltas.dropna().max() <= max_delta_per_s
