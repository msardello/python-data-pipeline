from fastapi import FastAPI
from scripts.pipeline_api import run_pipeline_api
import json

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI-SE-Assistant API is running!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/pipeline")
def run_default_pipeline():
    # Default values for the pipeline
    csv_path = "data/opportunities.csv"
    top_n = 5
    min_amount = None
    stage = None

    return run_pipeline_api(csv_path, top_n, min_amount, stage)


@app.get("/pipeline/custom", summary="Run Custom Pipeline")
def run_custom_pipeline(
    csv_path: str = "data/opportunities.csv",
    # csv_path: str,
    top_n: int = 5,
    # top_n: int,
    min_amount: int | None = None,
    stage: str | None = None,
):
    """
    Runs the pipeline with custom filters:
    - min_amount: filter rows >= this amount
    - stage: filter rows matching this stage
    """

    return run_pipeline_api(
        csv_path=csv_path, top_n=top_n, min_amount=min_amount, stage=stage
    )
