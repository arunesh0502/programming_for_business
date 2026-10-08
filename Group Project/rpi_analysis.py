#--------Import
import pandas as pd
import matplotlib.pyplot as plt
 
# --------Load the cleaned dataset (saved by Data_Cleaning.py)
rpi = pd.read_csv("Cleaned_Dataset.csv")
 
# Shared data for Tasks 1 to 3: the years 2019-2025 (2019, 2021, 2023 and 2025 exist)
four_years = rpi[(rpi["YEAR"] >= 2019) & (rpi["YEAR"] <= 2025)].copy()
four_years["TOWN (REGION)"] = four_years["TOWN LOCALITY"] + " (" + four_years["REGION"] + ")"
 
# Shared functions for Tasks 1 to 3
def top_n_by_year(data, value_col, n):
    """Return the n highest value_col rows in each year, best first."""
    result = pd.DataFrame()
    for year in sorted(data["YEAR"].unique()):
        year_rows = data[data["YEAR"] == year].sort_values(value_col, ascending=False)
        result = pd.concat([result, year_rows.head(n)])
        result.index = range(1, len(result) + 1) 
    return result
 
def average_by_region(data):
    """Return the mean ALL GROUPS (2 dp) per region per year, and the number of towns behind it."""
    grouped = data.groupby(["YEAR", "REGION"])["ALL GROUPS"]
    averages = grouped.mean().round(2).reset_index(name="avg_all_groups")
    towns = grouped.count().reset_index(name="n_towns")
    return pd.concat([averages, towns["n_towns"]], axis=1)
 
def compare_top_levels(top1_region, top1_town):
    """Put the highest region and the highest town of each year side by side."""
    region_part = top1_region[["YEAR", "REGION", "avg_all_groups"]]
    region_part.columns = ["YEAR", "TOP REGION", "REGION AVG"]
    town_part = top1_town[["YEAR", "TOWN LOCALITY", "REGION", "ALL GROUPS"]]
    town_part.columns = ["YEAR", "TOP TOWN", "TOWN'S REGION", "TOWN VALUE"]
    comparison = region_part.merge(town_part, on="YEAR")
    comparison["GAP"] = comparison["TOWN VALUE"] - comparison["REGION AVG"].round(2)
    comparison["SAME REGION"] = comparison["TOP REGION"] == comparison["TOWN'S REGION"]
    comparison.index = range(1, len(comparison) + 1) 
    return comparison
 
# --------Task 1
# Top three Town Localities for each year 2019-2025
top_towns = top_n_by_year(four_years, "ALL GROUPS", 3)[["YEAR", "TOWN (REGION)", "ALL GROUPS"]]
print(top_towns)
 
# --------Task 2
# Top three Regions for each year 2019-2025
region_avg = average_by_region(four_years)
top3_regions = top_n_by_year(region_avg, "avg_all_groups", 3)
print(top3_regions)
 
# Highest region and highest town in each year 2019-2025
top1_region = top_n_by_year(region_avg, "avg_all_groups", 1)
top1_town = top_n_by_year(four_years, "ALL GROUPS", 1)
 
# Highest region against highest town, year by year
level_comparison = compare_top_levels(top1_region, top1_town)
print(level_comparison)
 
# Tables in the shape the Task 5 charts expect (label column + ALL GROUPS)
top_regions = top3_regions.rename(columns={"avg_all_groups": "ALL GROUPS"})[["YEAR", "REGION", "ALL GROUPS"]]
best_town = top1_town[["YEAR", "TOWN (REGION)", "ALL GROUPS"]].set_index("YEAR")
best_region = top1_region.rename(columns={"avg_all_groups": "ALL GROUPS"})[["YEAR", "REGION", "ALL GROUPS"]].set_index("YEAR")
 
# --------Task 3
# Median ALL GROUPS of all towns in each year, then remove the towns below it
def yearly_median(data):
    """Return the median ALL GROUPS of all towns for each year."""
    return data.groupby("YEAR")["ALL GROUPS"].median().round(2).reset_index(name="median_rpi")
 
def remove_below_median(data, medians):
    """Keep only the towns at or above their year's median (a town on the median is not below it)."""
    merged = data.merge(medians, on="YEAR")
    return merged[merged["ALL GROUPS"] >= merged["median_rpi"]].reset_index(drop=True)
 
medians = yearly_median(four_years)
trimmed = remove_below_median(four_years, medians)
 
# Evidence: towns before and after, per year
towns_before = four_years.groupby("YEAR")["ALL GROUPS"].count().reset_index(name="towns_before")
towns_after = trimmed.groupby("YEAR")["ALL GROUPS"].count().reset_index(name="towns_after")
median_summary = pd.concat([medians, towns_before["towns_before"], towns_after["towns_after"]], axis=1)
median_summary.index = range(1, len(median_summary) + 1) 
print(median_summary)
 
# Repeat Task 2 on the trimmed towns, with the same functions
trimmed_avg = average_by_region(trimmed)
trimmed_top3 = top_n_by_year(trimmed_avg, "avg_all_groups", 3)
trimmed_top1_region = top_n_by_year(trimmed_avg, "avg_all_groups", 1)
trimmed_top1_town = top_n_by_year(trimmed, "ALL GROUPS", 1)
print(trimmed_top3)
print(compare_top_levels(trimmed_top1_region, trimmed_top1_town))
 
# Original against trimmed top three regions, side by side
difference = pd.concat([top3_regions[["YEAR", "REGION", "avg_all_groups"]],
                        trimmed_top3[["REGION", "avg_all_groups", "n_towns"]]], axis=1)
difference.columns = ["YEAR", "ORIGINAL REGION", "ORIGINAL AVG", "TRIMMED REGION", "TRIMMED AVG", "TOWNS KEPT"]
difference["SAME REGION"] = difference["ORIGINAL REGION"] == difference["TRIMMED REGION"]
print(difference)


# --------Tasks 5

# Colours tell the story: Kimberley (blue) and Pilbara (red) are the two regions that keep
# topping the index, so they get the strongest colours; Gascoyne (teal) and Goldfields-Esperance
# (gold) only appear now and then; any other region would be grey. A town takes its region's colour.
region_colour = {"Kimberley": "#0840F7", "Pilbara": "#D40101",
                 "Gascoyne": "#12D4BE", "Goldfields-Esperance": "#E2A808"}
town_region = four_years.set_index("TOWN (REGION)")["REGION"].to_dict()


# Function for the four bar charts: one group of bars per year, best first
def bar_chart(data, label_col, title, filename):
    years = sorted(data["YEAR"].unique())
    shown = []

    the_fig = plt.figure(figsize=(12, 5.5))
    the_ax = the_fig.subplots()

    for i in range(len(years)):
        rows = data[data["YEAR"] == years[i]]
        for j in range(len(rows)):
            row = rows.iloc[j]
            region = row[label_col] if label_col == "REGION" else town_region[row[label_col]]
            label = "_" + region if region in shown else region  # a leading "_" keeps repeats out of the legend
            shown.append(region)
            x = i + (j - (len(rows) - 1) / 2) * 0.3
            bar = the_ax.bar(x, row["ALL GROUPS"], width=0.28, color=region_colour.get(region, "grey"), label=label)
            name = row[label_col].split(" (")[0].replace(" ", "\n").replace("-", "-\n")
            the_ax.bar_label(bar, labels=[name + "\n" + f"{row['ALL GROUPS']:.2f}"], fontsize=8)  # name and value on each bar

    the_ax.set_xticks(range(len(years)), years)  # one tick per year
    the_ax.set_title(title)
    the_ax.set_xlabel("Year")
    the_ax.set_ylabel("Regional Price Index (All Groups)")
    the_ax.set_ylim(0, 170)
    the_ax.legend(loc="upper left", ncol=4, frameon=False)
    plt.tight_layout()
    the_fig.savefig(filename, dpi=300)

# Chart 1: top three towns each year (Task 1)
bar_chart(top_towns, "TOWN (REGION)", "Task 1: Top three towns by Regional Price Index (All Groups)", "task1_top_towns.png")

# Chart 2: top three regions each year (Task 2)
bar_chart(top_regions, "REGION", "Task 2: Top three regions by average Regional Price Index (All Groups)", "task2_top_regions.png")

# Chart 3: highest town each year (Task 2)
bar_chart(best_town.reset_index(), "TOWN (REGION)", "Task 2: Highest town by Regional Price Index (All Groups)", "task2_highest_town.png")

# Chart 4: highest region each year (Task 2)
bar_chart(best_region.reset_index(), "REGION", "Task 2: Highest region by average Regional Price Index (All Groups)", "task2_highest_region.png")

# Task 3 charts: the same bar_chart, on the towns left after removing those below the median
trimmed_regions = trimmed_top3.rename(columns={"avg_all_groups": "ALL GROUPS"})[["YEAR", "REGION", "ALL GROUPS"]]
trimmed_best_region = trimmed_top1_region.rename(columns={"avg_all_groups": "ALL GROUPS"})[["YEAR", "REGION", "ALL GROUPS"]]
#trimmed_best_town = trimmed_top1_town[["YEAR", "TOWN (REGION)", "ALL GROUPS"]]

bar_chart(trimmed_regions, "REGION", "Task 3: Top three regions by average Regional Price Index after removing towns below the median", "task3_top_regions.png")
bar_chart(trimmed_best_region, "REGION", "Task 3: Highest region after removing towns below the median", "task3_highest_region.png")
#bar_chart(trimmed_best_town, "TOWN (REGION)", "Task 3: Highest town after removing towns below the median", "task3_highest_town.png")

plt.show()