from fastapi import FastAPI
from pydantic import BaseModel
from scripts.pipeline_api import run_pipeline_api
from scripts.config import load_settings

app = FastAPI(title="AI SE Assistant Pipeline API")


# Request model for /pipeline/custom
class PipelineRequest(BaseModel):
    csv_path: str | None = None
    top_n: int | None = None
    min_amount: float | None = None
    stage: str | None = None


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/pipeline")
def run_default_pipeline():
    """Run pipeline with default config values."""
    settings = load_settings()

    results = run_pipeline_api(
        csv_path=settings["default_csv"],
        top_n=settings["default_top_n"],
    )

    return results


@app.post("/pipeline/custom")
def run_custom_pipeline(request: PipelineRequest):
    """Run pipeline with optional custom parameters."""

    results = run_pipeline_api(
        csv_path=request.csv_path,
        top_n=request.top_n,
        min_amount=request.min_amount,
        stage=request.stage,
    )

    return results
