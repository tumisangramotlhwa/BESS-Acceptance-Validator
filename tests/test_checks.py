import pandas as pd
import numpy as np
from validator.checks import check_std, check_bounds, check_ramp_rate


def test_check_std_passes():
    s = pd.Series([100, 101, 99, 100])
    assert check_std(s, max_std=2.0)


def test_check_bounds_fails():
    s = pd.Series([49.9, 50.0, 50.3])
    assert not check_bounds(s, min_val=49.8, max_val=50.2)


def test_check_ramp_rate_detects_spike():
    s = pd.Series([0, 0, 200])
    assert not check_ramp_rate(s, max_delta_per_s=50, dt_s=1.0)