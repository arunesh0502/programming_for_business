import pandas as pd

df = pd.read_excel("appendix8.xlsx", sheet_name="Table 8.7")

df= df.dropna()  # Drop rows with any missing values
df= df.iloc[1:]  # Drop the first row (header row)

# Filter out rows with values "-(d)" and "-"
df= df[~(df["Unnamed: 6"] == "-")]
df= df[~(df["Unnamed: 6"] == "-(d)")]
df= df[~(df["Unnamed: 2"] == "-")]


# Task C: Change the Column Names
df.columns = ["Item Detail", "Department", "FY15", "FY16", "FY17", "FY18", "FY19"]

# Task D: Remove (b)
df["FY16"] = df["FY16"].astype(str).str.replace("(b)","", regex=False)

# Task E: Convert the columns to numeric values
df[["FY15", "FY16", "FY17", "FY18", "FY19"]] = df[["FY15", "FY16", "FY17", "FY18", "FY19"]].astype(float)

# Task F: Group the data by "Department" and calculate the sum for each fiscal year, and remove the Item Detail column
df = df.groupby("Department")[["FY15", "FY16", "FY17", "FY18", "FY19"]].sum()

# Task G: Sort from Highest to Lowest based on FY19
df = df.sort_values("FY19", ascending=False)

df.to_csv("processed_data1.csv", index=False)  

print(df)