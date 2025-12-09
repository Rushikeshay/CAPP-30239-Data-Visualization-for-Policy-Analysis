import pandas as pd
import re

# Load data
df = pd.read_excel("Global Protest Tracker.xlsx")

# Extract 2-digit year, 4-digit year, and month
def parse_date(val):
    text = str(val)

    # year (2 digits)
    y2 = re.search(r"\d{2}", text)
    y2 = y2.group(0) if y2 else None

    # convert to 4-digit
    if y2:
        y2_int = int(y2)
        y4 = 2000 + y2_int if y2_int <= 29 else 1900 + y2_int
    else:
        y4 = None

    # month
    m = re.search(r"[A-Za-z]{3}", text)
    m = m.group(0).title() if m else None

    return pd.Series([y2, y4, m])

# Apply once
df[["Year_2digit", "Year_4digit", "Month"]] = df["Start Date"].apply(parse_date)
df["Year_4digit"] = df["Year_4digit"].astype("Int64")
df["MonthYear"] = df["Month"] + "-" + df["Year_2digit"].astype(str)

# Fix country names for mapping
df["Country"] = df["Country"].replace({
    "United States": "United States of America",
    "Central African Republic": "Central African Rep.",
    "South Sudan": "S. Sudan",
    "Democratic Republic of the Congo": "Dem. Rep. Congo"
})

# Final export (only once)
df.to_csv("protest.csv", index=False)
