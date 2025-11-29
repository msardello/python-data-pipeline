from scripts.pipeline_core import run_pipeline_core
from scripts.config import load_settings


def run_pipeline_api(
    csv_path=None,
    top_n=None,
    min_amount=None,
    stage=None,
    validate_only=False,
):
    """
    API wrapper for the shared pipeline_core.
    """

    settings = load_settings()

    # Apply defaults if API did not supply values
    if csv_path is None:
        csv_path = settings["default_csv"]

    if top_n is None:
        top_n = settings["default_top_n"]

    # Call the unified core pipeline
    results = run_pipeline_core(
        csv_path=csv_path,
        top_n=top_n,
        validate_only=validate_only,
        min_amount=min_amount,
        stage=stage,
    )

    return results
