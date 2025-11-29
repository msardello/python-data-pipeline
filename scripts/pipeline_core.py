import pandas as pd
from scripts.utils import safe_load_csv, validate_opportunity_data
from scripts.opportunity_functions import (
    pipeline_summary,
    pipeline_by_owner,
    top_n_deals,
)


def load_and_filter(csv_path, min_amount=None, stage=None):
    """
    Shared loader + optional filter logic.
    Used by both CLI and API.
    """

    df = safe_load_csv(csv_path)

    # Apply optional filters
    if min_amount is not None:
        df = df[df["Amount"] >= min_amount]

    if stage is not None:
        df = df[df["Stage"] == stage]

    return df


def generate_results(df, top_n):
    """
    Shared results generator.
    Produces consistent JSON structure for CLI and API.
    """

    summary = pipeline_summary(df)

    owners = pipeline_by_owner(df).to_dict(orient="records")
    top_deals = top_n_deals(df, top_n).to_dict(orient="records")

    return {
        "summary": summary,
        "pipeline_by_owner": owners,
        f"top_{top_n}_deals": top_deals,
    }


def run_pipeline_core(
    csv_path, top_n, min_amount=None, stage=None, validate_only=False
):
    """
    Main shared function for CLI & API.
    """

    # Load & filter
    df = load_and_filter(csv_path, min_amount=min_amount, stage=stage)

    # Validation
    if validate_only:
        validate_opportunity_data(df)
        return {"validation": "passed"}

    validate_opportunity_data(df)

    # Build results dict
    return generate_results(df, top_n)
