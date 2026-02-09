# Acceptance Validator

A Python tool for validating and visualizing utility-scale BESS telemetry. During utility-scale BESS commissioning and acceptance testing, engineers must verify that telemetry (power, frequency, voltage) meets contractual and grid-code acceptance criteria. In practice, real telemetry often contains dropouts, timing gaps, and noise that complicate validation and reporting.

This tool was built to automate acceptance-style checks on BESS telemetry and generate clear, engineer-readable outputs for commissioning and validation workflows.

## Features

- Generate synthetic BESS telemetry (power, voltage, current, frequency)
- Evaluate data against acceptance criteria (ramp rates, frequency bounds)
- Handle telemetry dropouts and fill missing values with a rolling average
- Visualize before/after filled data with filled samples explicitly marked

## Typical Use Case:

- Engineer receives BESS telemetry from commissioning or HiL testing

- Acceptance criteria are defined in a YAML ruleset

- Validator flags violations (ramp rate, frequency bounds, etc.)

- Dropouts are handled deterministically and explicitly marked

- Plots and summaries are generated for acceptance review

## Requirements

- Python 3.10+
- pip

Install dependencies:

pip install -r requirements.txt

## Repository Structure
```

acceptance-validator/
├─ validator/                 # Python package
├─ data/                      # Example CSV files
├─ criteria/                  # Example acceptance criteria
├─ scripts/                   # Pipeline scripts
├─ requirements.txt
└─ README.md
```

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