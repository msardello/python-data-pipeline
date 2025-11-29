from scripts.utils import safe_load_csv
from scripts.opportunity_functions import (
    # proposal_opportunities,
    win_rate,
    pipeline_by_owner,
    top_n_deals,
)


def run_pipeline_api(csv_path, top_n, min_amount=None, stage=None):
    df = safe_load_csv(csv_path)

    # Apply optional filters
    if min_amount is not None:
        df = df[df["Amount"] >= min_amount]

    if stage is not None:
        df = df[df["Stage"] == stage]

    # Return JSON-friendly summary
    return {
        # "proposal_opportunities": proposal_opportunities(df).to_dict(orient="records"),
        "win_rate": win_rate(df),
        "pipeline_by_owner": pipeline_by_owner(df).to_dict(orient="records"),
        "top_deals": top_n_deals(df, top_n).to_dict(orient="records"),
    }
