import pandas as pd
import matplotlib.pyplot as plt

car_df = pd.read_csv("mtcars.csv")

# print(car_df)

# Question a. A scatter plot, comparing displacement and horsepower for all vehicles, 
# with each scatter plot blue in colour and with an appropriate title and axis labels

#plt.scatter(car_df["displacement"], car_df["horsepower"], color="blue")

#plt.title("Displacement vs Horsepower")
#plt.xlabel("Displacement")
#plt.ylabel("Horsepower")

car_df.plot(kind="scatter", x="displacement", y="horsepower", color="blue")
the_ax = plt.gca()
the_fig = plt.gcf()
the_ax.set_title("Displacement vs Horsepower")
the_ax.set_xlabel("Displacement")
the_ax.set_ylabel("Horsepower")
the_fig.savefig("displacement_vs_horsepower.png")
plt.show()

