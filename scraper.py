import requests
import pandas as pd
from io import StringIO

# Innings-by-innings fielding URL
url = "https://stats.espncricinfo.com/ci/engine/player/35320.html?class=11;template=results;type=fielding;view=innings"

# Browser headers to avoid 403
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

# Fetch page
response = requests.get(url, headers=headers)
response.raise_for_status()

html = response.text

# Read all tables from the page
tables = pd.read_html(StringIO(html))

print(f"Total tables found: {len(tables)}")

# Identify the innings-by-innings batting table
batting_df = None

for table in tables:
    cols = table.columns.astype(str)
    if "Runs" in cols and "Opposition" in cols: #if fielding then Change "Runs" to "Inns"
        batting_df = table
        break

if batting_df is None:
    raise Exception("Innings-by-innings fielding table not found!")

# Clean column names
batting_df.columns = batting_df.columns.astype(str).str.strip()

# Remove blank rows
batting_df = batting_df[batting_df["Runs"].notna()] #if fielding then Change "Runs" to "Inns"

# Display sample
print("\nInnings by innings data:")
print(batting_df.head())

# Save to CSV
batting_df.to_csv("sachin_Fielding_summary.csv", index=False)
print("\n✅ File saved: sachin_Fielding_summary.csv")