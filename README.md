# Acceptance Validator

A Python tool for validating and visualizing utility-scale BESS telemetry.

## Features

- Generate synthetic BESS telemetry (power, voltage, current, frequency)
- Evaluate data against acceptance criteria (ramp rates, frequency bounds)
- Handle telemetry dropouts and fill missing values with a rolling average
- Visualize before/after filled data with filled samples explicitly marked

## Requirements

- Python 3.10+
- pip

Install dependencies:

pip install -r requirements.txt

## Repository Structure

acceptance-validator/
├─ validator/                 # Python package
├─ data/                      # Example CSV files
├─ criteria/                  # Example acceptance criteria
├─ scripts/                   # Pipeline scripts
├─ requirements.txt
└─ README.md

## Run the full pipeline

This will:
1. Generate synthetic telemetry
2. Run acceptance validation
3. Produce plots (original + filled)

python scripts/run_full_pipeline.py

## Run validator only

python -m validator.cli --data data/synthetic_bess_commissioning.csv --criteria criteria/example.yaml

## Outputs

- bess_original.png – raw telemetry
- bess_filled.png – telemetry with filled dropouts marked
- Console summary of acceptance test results

Filled samples are marked with **×** symbols.

## Notes

- Do **not modify CSV paths manually**; the CLI handles paths via --data
- Use --criteria to point to different YAML rulesets