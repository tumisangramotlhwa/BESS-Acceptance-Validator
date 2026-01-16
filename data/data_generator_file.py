import requests
import numpy as np
import pandas as pd

def generate_bess_timeseries(
    duration_s: int = 300,
    sample_hz: float = 1.0,
    seed: int = 42,
    inject_ramp_violation: bool = True,
    inject_dropouts: bool = True,
) -> pd.DataFrame:
    """

    Signals:
    - power_kw
    - voltage_v
    - current_a
    - frequency_hz

    """

    rng = np.random.default_rng(seed)
    n = int(duration_s * sample_hz)
    t = np.arange(n) / sample_hz

    timestamps = pd.date_range(
        start="2026-01-01",
        periods=n,
        freq=pd.Timedelta(seconds=1 / sample_hz)
    )

    # frequency 
    frequency_hz = 50.0 + rng.normal(0, 0.03, size=n)

    # power profile (slow ramp + small noise)
    power_kw = np.linspace(500, 800, n) + rng.normal(0, 2.0, size=n)

    # inject a ramp-rate violation
    if inject_ramp_violation:
        idx = int(0.6 * n)
        power_kw[idx:idx + 2] += 250  # unrealistic step

    # voltage (stiff, mildly noisy)
    voltage_v = 1000 + rng.normal(0, 5.0, size=n)

    # current
    current_a = (power_kw * 1000) / voltage_v
    current_a += rng.normal(0, 1.5, size=n)

    # inject telemetry dropouts
    if inject_dropouts:
        drop_idx = slice(int(0.75 * n), int(0.78 * n))
        power_kw[drop_idx] = np.nan
        frequency_hz[drop_idx] = np.nan

        # fill missing power_kw with moving average (centered)
        power_kw_series = pd.Series(power_kw)
        power_kw_filled = power_kw_series.fillna(
            power_kw_series.rolling(window=3, min_periods=1, center=True).mean()
    )
    power_kw[:] = power_kw_filled.values

    # fill missing frequency_hz with moving average (centered)
    frequency_series = pd.Series(frequency_hz)
    frequency_filled = frequency_series.fillna(
        frequency_series.rolling(window=3, min_periods=1, center=True).mean()
    )
    frequency_hz[:] = frequency_filled.values

    df = pd.DataFrame({
        "timestamp": timestamps,
        "power_kw": power_kw,
        "voltage_v": voltage_v,
        "current_a": current_a,
        "frequency_hz": frequency_hz,
    })

    return df


if __name__ == "__main__":
    df = generate_bess_timeseries()
    df.to_csv("synthetic_bess_commissioning.csv", index=False)
    print("Generated synthetic_bess_commissioning.csv")