import pandas as pd

# Load CSV files
batting = pd.read_csv("D:\Ram\Sachin\sachin_batting_summary.csv")
bowling = pd.read_csv("D:\Ram\Sachin\sachin_bowling_summary.csv")
fielding = pd.read_csv("D:\Ram\Sachin\sachin_Fielding_summary.csv")

# Left join batting with bowling
bat_bowl = pd.merge(
    batting,
    bowling,
    on=["ID", "Match #"],
    how="left"
)

# Left join the result with fielding
final_df = pd.merge(
    bat_bowl,
    fielding,
    on=["ID", "Match #"],
    how="left"
)

# Preview
print(final_df.head())

# Save output
final_df.to_csv("sachin_left_join_summary.csv", index=False)
print("\n✅ File saved: sachin_left_join_summary.csv")