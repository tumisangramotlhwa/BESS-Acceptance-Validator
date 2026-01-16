import subprocess
from pathlib import Path
from validator.report import visualize_bess
from validator.cli import main as run_validator
from data.data_generator_file import generate_bess_timeseries

def main():
    output_csv = Path("data/synthetic_bess_commissioning.csv")
    output_csv.parent.mkdir(exist_ok=True)

    df = generate_bess_timeseries()
    df.to_csv(output_csv, index=False)
    print(f"Generated synthetic data: {output_csv}")

    criteria_file = Path("criteria/example.yaml")

    print("\nRunning validator CLI...")
    subprocess.run([
        "py", "-m", "validator.cli",
        "--data", str(output_csv),
        "--criteria", str(criteria_file)
    ], check=False)

    print("\nGenerating before/after plots...")
    visualize_bess(output_csv, filled=False)
    visualize_bess(output_csv, filled=True)

    print("\nPipeline complete!")
    print("Plots saved as bess_before_fill.png and bess_after_fill.png")

if __name__ == "__main__":
    main()