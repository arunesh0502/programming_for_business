import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel("appendix8.xlsx", sheet_name="Table 8.7")

df= df.dropna()  # Drop rows with any missing values

# Filter out rows with values "-(d)" and "-"
df= df[~(df["Unnamed: 6"] == "-")]
df= df[~(df["Unnamed: 6"] == "-(d)")]
df= df[~(df["Unnamed: 2"] == "-")]

# Filter out rows where less than or equal to 5 million
data_cols = ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6"]
df[data_cols] = df[data_cols].apply(pd.to_numeric, errors='coerce')
df= df[(df["Unnamed: 6"] >= 5)]

print(df)
print(df.describe())

# Save the filtered DataFrame to a CSV file
df.to_csv("processed_data.csv", index=False)  
