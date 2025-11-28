import pandas as pd
import os
from scripts.config import load_settings


def safe_load_csv(path):
    """Load a CSV with error handling and whitespace cleanup."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV not found at: {path}")

    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Could not read CSV: {e}")

    # Clean column names
    df.columns = [col.strip() for col in df.columns]

    return df


def validate_opportunity_data(df):
    settings = load_settings()

    # required_cols = ["Name", "Owner", "Stage", "Amount"]

    required_cols = settings["required_columns"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column {col}")

    # if df["Amount"].type not in ["int64", "float64"]:
    #     raise ValueError("Column 'Amount' must be numeric")
    if df["Amount"].dtype.kind not in ["i", "u", "f"]:
        raise ValueError("Column 'Amount' must be numeric")

    return True
