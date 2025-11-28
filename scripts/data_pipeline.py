import json
import pandas as pd
import logging
from scripts.config import load_settings

logging.basicConfig(
    filename="outputs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


from scripts.utils import safe_load_csv, validate_opportunity_data
from scripts.opportunity_functions import (
    pipeline_summary,
    top_n_deals,
    pipeline_by_owner,
)


# def run_pipeline(input_csv, output_dir="outputs", top_n=3, validate_only=False):
def run_pipeline(input_csv=None, top_n=None, validate_only=False):

    settings = load_settings()

    # Override default CSV if provide via CLI
    if input_csv is None:
        input_csv = settings["default_csv"]

    # Override default top N if provided via CLI
    if top_n is None:
        top_n = settings["default_top_n"]

    # Output directory always comes from config
    output_dir = settings["output_dir"]

    print("\n=== PIPELINE CONFIGURATION ===")
    print(f"Using CSV: {input_csv}")
    print(f"Top N deals: {top_n}")
    print(f"Output directory: {output_dir}")
    print("==============================\n")

    print("\n=== RUNNING DATA PIPELINE ===")

    # Step 1: Load the data safely
    df = safe_load_csv(input_csv)
    # print("Loaded CSV successfully.")
    logging.info("Loaded CSV successfully.")

    # Step 2: Validate required columns
    validate_opportunity_data(df)
    if validate_only:
        print("Validation complete. No further processing requested.")
        return
    # print("Data validation passed.")
    logging.info("Data validations passed.")

    # Step 3: Generate summary objects
    summary = pipeline_summary(df)
    owners = pipeline_by_owner(df).to_dict(orient="records")
    # top3 = top_n_deals(df, top_n).to_dict(orient="records")
    top_deals = top_n_deals(df, top_n).to_dict(orient="records")

    # Step 4: Save results
    results = {
        "summary": summary,
        "pipeline_by_owner": owners,
        f"top_{top_n}_deals": top_deals,
    }

    output_path = f"{output_dir}/pipeline_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    logging.info("Save pipeline results.")

    print(f"Pipeline results saved to {output_path}")
    return results


# if __name__ == "__main__":
#     run_pipeline("data/opportunities.csv")
# import sys

# if __name__ == "__main__":
#     input_file = sys.argv[1] if len(sys.argv) > 1 else "data/opportunities.csv"
#     run_pipeline(input_file)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process opportunity data and generate pipeline summaries."
    )

    parser.add_argument(
        "--input",
        type=str,
        # default="data/opportunities.csv",
        # help="Path to the input CSV file",
        help="Optional: override default CSV file from config.yaml",
    )

    parser.add_argument(
        "--top",
        type=int,
        # default=3,
        help="Optional: override default top N from config.yaml",
    )

    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the CSV and exit (skip procssing)",
    )

    args = parser.parse_args()

    run_pipeline(input_csv=args.input, top_n=args.top, validate_only=args.validate_only)
