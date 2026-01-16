from typing import List
import pandas as pd
import matplotlib.pyplot as plt

def print_summary(results: List[dict]) -> None:
    print("\nAcceptance Test Results")
    print("=" * 30)

    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"{r['name']:<25} {status}")

    if not all(r["passed"] for r in results):
        raise SystemExit(1)


def visualize_bess(csv_path: str, filled: bool = False) -> None:

    df = pd.read_csv(csv_path, parse_dates=["timestamp"])

    # dropout locations before filling
    nan_mask = df["power_kw"].isna() | df["frequency_hz"].isna()

    # apply rolling-average fill
    if filled:
        for col in ["power_kw", "frequency_hz"]:
            df[col] = df[col].fillna(
                df[col]
                .rolling(window=3, min_periods=1, center=True)
                .mean()
            )

    plt.figure(figsize=(14, 8))

    plt.plot(df["timestamp"], df["power_kw"], label="Power (kW)", linewidth=2)
    plt.plot(df["timestamp"], df["frequency_hz"], label="Frequency (Hz)", linewidth=2)
    plt.plot(df["timestamp"], df["voltage_v"], label="Voltage (V)", alpha=0.5)
    plt.plot(df["timestamp"], df["current_a"], label="Current (A)", alpha=0.5)

    # mark filled samples explicitly
    if filled and nan_mask.any():
        plt.scatter(
            df.loc[nan_mask, "timestamp"],
            df.loc[nan_mask, "power_kw"],
            color="black",
            marker="x",
            s=60,
            label="Filled samples",
            zorder=5
        )

    title = "BESS Telemetry"
    title += " (Filled Dropouts)" if filled else " (Original)"

    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = "bess_filled.png" if filled else "bess_original.png"
    plt.savefig(filename)
    plt.close()

    print(f"Saved {filename}")


