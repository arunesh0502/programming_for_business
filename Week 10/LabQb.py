# Question b. A bar chart, comparing the average quarter mile time for cars from each of the 
# countries of origin, with the bars red in colour and with an appropriate title and axis labels

import pandas as pd
import matplotlib.pyplot as plt

car_df = pd.read_csv("mtcars.csv")

newcar_df = car_df.groupby("country-origin")["qtrmile-secs"].mean().reset_index()
newcar_df.plot(kind="bar", x="country-origin", y="qtrmile-secs", color="red")
the_ax = plt.gca()
the_fig = plt.gcf()
the_ax.set_title("Average Quarter Mile Time by Country of Origin")
the_ax.set_xlabel("Country of Origin")  
the_ax.set_ylabel("Quarter-Mile Time (seconds)")
plt.tight_layout()
the_fig.savefig("avg_qtrmile_time_by_country.png")


#newcar_df.plot(kind="bar", color="red")
#plt.title("Average Quarter-Mile Time by Country of Origin")
#plt.xlabel("Country of Origin")
#plt.ylabel("Average Quarter-Mile Time (seconds)")
#plt.show()
