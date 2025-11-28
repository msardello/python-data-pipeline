from scripts.utils import safe_load_csv
import pandas as pd
import os


def test_safe_load_csv(tmp_path):
    # Create a temporary CSV
    p = tmp_path / "sample.csv"
    p.write_text("Name,Owner,Stage,Amount\nA,B,C,100")

    df = safe_load_csv(str(p))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert "Amount" in df.columns
