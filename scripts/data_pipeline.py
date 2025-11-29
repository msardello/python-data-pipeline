import json
import logging
import argparse
from scripts.config import load_settings
from scripts.pipeline_core import run_pipeline_core


logging.basicConfig(
    filename="outputs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_pipeline(
    csv_path=None,
    top_n=None,
    validate_only=False,
    min_amount=None,
    stage=None,
):
    """CLI wrapper that delegates to pipeline_core."""

    settings = load_settings()

    # CLI overrides config defaults
    if csv_path is None:
        csv_path = settings["default_csv"]

    if top_n is None:
        top_n = settings["default_top_n"]

    print("\n=== PIPELINE CONFIGURATION ===")
    print(f"Using CSV: {csv_path}")
    print(f"Top N deals: {top_n}")
    print(f"validate_only: {validate_only}")
    print(f"min_amount: {min_amount}")
    print(f"stage filter: {stage}")
    print("==============================\n")

    # Call shared pipeline core
    results = run_pipeline_core(
        csv_path=csv_path,
        top_n=top_n,
        validate_only=validate_only,
        min_amount=min_amount,
        stage=stage,
    )

    # If validation-only, stop here
    if validate_only:
        print("Validation passed. No further processing.")
        return results

    # Save output
    output_path = f"{settings['output_dir']}/pipeline_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Pipeline results saved to: {output_path}")
    logging.info("Pipeline results saved.")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Opportunity data pipeline CLI")

    parser.add_argument("--input", type=str, help="Override CSV path")
    parser.add_argument("--top", type=int, help="Override top N")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--min-amount", type=float)
    parser.add_argument("--stage", type=str)

    args = parser.parse_args()

    run_pipeline(
        csv_path=args.input,
        top_n=args.top,
        validate_only=args.validate_only,
        min_amount=args.min_amount,
        stage=args.stage,
    )
