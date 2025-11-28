import pandas as pd

# Load CSV
df = pd.read_csv("data/opportunities.csv")

# Basic totals
total_opps = len(df)
unique_owners = df["Owner"].nunique()
total_pipeline = df["Amount"].sum()

# Group by owner
by_owner = df.groupby("Owner")["Amount"].sum().reset_index()

print("\n=== PIPELINE SUMMARY ===")
print(f"Total Opportunities: {total_opps}")
print(f"Unique Owners: {unique_owners}")
print(f"Total Pipeline Value: ${total_pipeline:,.0f}")

print("\n=== PIPELINE BY OWNER ===")
print(by_owner.to_string(index=False))
