# Question e. A line chart, showing the number of sales for each vehicle compared to the horsepower of the 
# vehicle, with the line coloured purple and appropriate axis labels and titles included

import pandas as pd
import matplotlib.pyplot as plt

car_df = pd.read_csv("mtcars.csv")

car_df = car_df.sort_values("fake-sales")
car_df.plot(kind="line", x="fake-sales", y="horsepower", color = "purple")
the_ax = plt.gca()
the_fig = plt.gcf()
the_ax.set_title("Fake Sales Compared to Horsepower")
the_ax.set_xlabel("Fake Sales")
the_ax.set_ylabel("Horsepower")
the_fig.savefig("fake_sales_horsepower.png")
plt.show()


