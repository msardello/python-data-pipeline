import pandas as pd

df = pd.read_csv("data/opportunities.csv")

# 1. Sort by Amount (descending)
sorted_df = df.sort_values(by="Amount", ascending=False)

print("\n=== SORTED BY AMOUNT (DESC) ===")
print(sorted_df.to_string(index=False))

# 2. Filter: Only Proposal Stage
proposal_df = df[df["Stage"] == "Proposal"]

print("\n=== PROPOSAL STAGE OPPORTUNITIES ===")
print(proposal_df.to_string(index=False))

# 3. Group: Count by Stage
stage_counts = df["Stage"].value_counts()

print("\n=== COUNT BY STAGE ===")
print(stage_counts)

# 4. Save a new CSV
sorted_df.to_csv("data/opportunities_sorted.csv", index=False)
proposal_df.to_csv("data/opportunities_proposals.csv", index=False)

# 5. Calculate Win Rate
closed_won = df[df["Stage"] == "Closed Won"]
win_rate = len(closed_won) / len(df)

print(f"\n=== WIN RATE ===")
print(f"Win Rate: {win_rate:.2%}")

# 6. Leaderboard by Owner
owner_leaderboard = df.groupby("Owner")["Amount"].sum().sort_values(ascending=False)

print("\n=== OWNER LEADERBOARD (BY TOTAL PIPELINE) ===")
print(owner_leaderboard)

# 7. Top 3 Deals
top3 = df.sort_values(by="Amount", ascending=False).head(3)

print("\n=== TOP 3 DEALS ===")
print(top3.to_string(index=False))
