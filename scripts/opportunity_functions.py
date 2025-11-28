import pandas as pd

df = pd.read_csv("data/opportunities.csv")


# Example of a simple reusable function
def total_pipeline(dataframe):
    return dataframe["Amount"].sum()


# Example of a function with a filter
def filter_by_stage(dataframe, stage_name):
    return dataframe[dataframe["Stage"] == stage_name]


# Example of a function with a calculation
def win_rate(dataframe):
    closed_won = dataframe[dataframe["Stage"] == "Closed Won"]
    return len(closed_won) / len(dataframe)


# Example of a function that returns a grouped summary
def pipeline_by_owner(dataframe):
    return dataframe.groupby("Owner")["Amount"].sum().reset_index()


# My example of adding to this file a new function
def top_n_deals(dataframe, n):
    return dataframe.sort_values(by="Amount", ascending=False).head(n)


def pipeline_summary(dataframe):
    total_opps = int(len(dataframe))
    total_pipeline = int(dataframe["Amount"].sum())
    wr = win_rate(dataframe)
    win_rate_percent = round(wr * 100, 2)

    summary = {
        "total_opps": total_opps,
        "total_pipeline": f"${total_pipeline:,.0f}",
        "win_rate": win_rate_percent,
    }
    return summary


# ---- Run the functions ----
print("\n=== TOTAL PIPELINE ===")
print(total_pipeline(df))

print("\n=== PROPOSAL OPPORTUNITIES ===")
print(filter_by_stage(df, "Proposal"))

print("\n=== WIN RATE ===")
print(win_rate(df))

print("\n=== PIPELINE BY OWNER ===")
print(pipeline_by_owner(df))

print("\n=== TOP 3 DEALS")
print(top_n_deals(df, 3))

# print("\n=== SUMMARY OBJECT ===")
# print(pipeline_summary(df))
