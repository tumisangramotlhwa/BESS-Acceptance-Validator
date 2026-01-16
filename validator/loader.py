import pandas as pd
import yaml
from pathlib import Path

def load_timeseries(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df = df.sort_values("timestamp")
    return df

def load_criteria(path: Path) -> dict:
    with open(path, "r") as file_contents:
        return yaml.load(file_contents, Loader=yaml.SafeLoader)

