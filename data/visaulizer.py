import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("synthetic_bess_commissioning.csv", parse_dates=["timestamp"])

plt.figure(figsize=(14, 8))

# Power
plt.plot(df['timestamp'], df['power_kw'], label='Power (kW)', color='blue')

# Frequency
plt.plot(df['timestamp'], df['frequency_hz'], label='Frequency (Hz)', color='orange')

# Voltage
plt.plot(df['timestamp'], df['voltage_v'], label='Voltage (V)', color='green', alpha=0.6)

# Current
plt.plot(df['timestamp'], df['current_a'], label='Current (A)', color='red', alpha=0.6)

# Plot formatting
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("BESS Telemetry Overview")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()