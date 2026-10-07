# Question d. A histogram, showing the frequency of cars within the dataset by the number of carburettors
# that the vehicle has, with the bars coloured green and with appropriate title and axis labels 

import pandas as pd
import matplotlib.pyplot as plt

car_df = pd.read_csv("mtcars.csv")
car_df = car_df.sort_values("carburettors")

plt.hist(car_df["carburettors"], color="green", edgecolor="black")

the_ax = plt.gca()
the_fig = plt.gcf()
the_ax.set_title("Frequency of Cars by Number of Carburettors")
the_ax.set_xlabel("Number of Carburettors")
the_ax.set_ylabel("Frequency")
the_fig.savefig("carburettor_frequency.png")
plt.show()

