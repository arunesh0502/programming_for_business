# Question c. A pie chart, showing the proportion of vehicles in the sample 
# (as a percentage) for each of the different values of cylinders represented, 
# with each of the pie segments a different colour and with an appropriate title and labels

import pandas as pd
import matplotlib.pyplot as plt

car_df = pd.read_csv("mtcars.csv")

newcar_df = car_df.groupby("cylinders").count().reset_index()
newcar_df.plot(kind="pie", x="cylinders", y="horsepower", autopct="%.1f%%")
the_ax = plt.gca()
the_fig = plt.gcf()
the_ax.set_title("Cylinder Distribution")
plt.tight_layout()
the_fig.savefig("cylinder_distribution.png")
plt.show()

#plt.pie(
#    cylinder_counts,
#    labels=cylinder_counts.index,
#    autopct="%1.1f%%")
#plt.title("Proportion of Vehicles by Number of Cylinders")
#plt.show()

