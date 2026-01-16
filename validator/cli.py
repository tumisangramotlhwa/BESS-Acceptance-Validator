import argparse
from pathlib import Path
from .loader import load_timeseries, load_criteria
from .evaluator import evaluate
from .report import print_summary, visualize_bess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--criteria", required=True)
    args = parser.parse_args()

    df = load_timeseries(Path(args.data))
    criteria = load_criteria(Path(args.criteria))

    results = evaluate(df, criteria)
    print_summary(results)

    visualize_bess(Path(args.data))

if __name__ == "__main__":
    main()
