from scripts.utils import safe_load_csv, validate_opportunity_data
from scripts.opportunity_functions import pipeline_summary

# 1: Load CSV safely
try:
    df = safe_load_csv("data/opportunities.csv")

    validate_opportunity_data(df)

    summary = pipeline_summary(df)

    # 2: Print results
    print("\n=== VALIDATED SUMMARY ===")
    print(summary)


except FileNotFoundError as fnf:
    print("ERROR: Missing CSV File")
    print(fnf)

except ValueError as ve:
    print("ERROR: Invalid CSV Format")
    print(ve)

except Exception as e:
    print("Unexpected Error:")
    print(e)
