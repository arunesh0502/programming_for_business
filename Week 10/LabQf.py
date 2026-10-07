# Question f. The most appropriate of a bar chart or a histogram, showing the frequency of each make within the dataset 
# (Hint: consider the first word of the model the make) with the bars coloured yellow, with an appropriate title and axis labels.

import pandas as pd
import matplotlib.pyplot as plt

car_df = pd.read_csv("mtcars.csv")

car_df["make"] = car_df["model"].str.split().str[0]

make_counts = car_df["make"].value_counts()

make_counts.plot(kind="bar", color="red")

the_ax = plt.gca()
the_fig = plt.gcf()
plt.title("Frequency of Vehicles by Make")
plt.xlabel("Make")
plt.ylabel("Frequency")
plt.tight_layout()
the_fig.savefig("make_frequency.png")
