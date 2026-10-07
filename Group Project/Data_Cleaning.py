import pandas as pd

# ==============================================================
# LOAD THE RAW DATASET
# ==============================================================
raw = pd.read_csv("RPI_raw.csv", skiprows=1) 
# Line 1 of the file is only a title ("REGIONAL PRICE INDEX"), so skiprows=1
# skips it and lets line 2 (TOWN LOCALITY, REGION, YEAR, ...) be the headings

raw.columns = raw.columns.str.strip().str.upper()
# Tidy the headings: remove stray spaces and force capitals so they match the code

print("Rows in raw file:", len(raw))
print(raw.columns)      

# ==============================================================
# STAGE 1: DATA CLEANING (raw DPIRD file -> cleaned DataFrame)
# ==============================================================

def remove_aggregate_rows(df):
    """
    Remove DPIRD's pre-computed regional summary rows.

    These are the rows where TOWN LOCALITY holds the same name as
    REGION (e.g. "Pilbara" in both columns). Keeping them would
    average a region's summary figure back into itself.

    df : raw DataFrame with TOWN LOCALITY and REGION columns
    Returns a copy of df without those rows.
    """
    town = df["TOWN LOCALITY"].str.strip().str.lower()
    region = df["REGION"].str.strip().str.lower()
    return df[town != region].copy()


def convert_to_numeric(df, index_cols):
    """
    Convert the index columns to numbers.

    The "-" placeholder cannot be read as a number, so errors="coerce"
    turns it into NaN. Blank cells are already NaN. Missing values are
    therefore kept as genuine nulls, NOT zero, so they are skipped
    when averages are calculated.

    df         : DataFrame to clean
    index_cols : list of the index column names to convert
    Returns df with those columns as numbers.
    """
    df[index_cols] = df[index_cols].apply(pd.to_numeric, errors="coerce")
    return df


def round_years(df):
    """
    Turn decimal years such as 2019.0000000000009 into whole years.
    df : DataFrame with a YEAR column
    Returns df with YEAR as whole numbers.
    """
    df["YEAR"] = df["YEAR"].astype(float).map(round)
    return df


index_cols = ["FOOD", "CLOTHING", "HOUSING", "HOUSEHOLD EQUIPMENT & OPERATION",
              "HOUSEHOLD SUPPLIES & SERVICES", "TRANSPORTATION",
              "TOBACCO & ALCOHOL", "HEALTH & PERSONAL CARE",
              "RECREATION & EDUCATION", "ALL GROUPS"]

# Applying the three cleaning steps in order
rpi = remove_aggregate_rows(raw)
print("Rows after removing aggregate rows:", len(rpi))
rpi = convert_to_numeric(rpi, index_cols)
rpi = round_years(rpi)

# Evidence that missing values are now NaN, not zero
print("Missing values per column:")
print(rpi.isna().sum())

# Save the cleaned dataset for reuse 
rpi.to_csv("Cleaned_Dataset.csv", index=False)
