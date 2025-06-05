import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# gets the data and sets x and y values
data = pd.read_csv("part1-linear-regression/chirping_data.csv")
print(data)
x = data["Temp"]
print(x)
y = data["Chirps"]
print(y)

# sets the size of the graph
plt.figure(figsize=(10,5))

# creates a scatter plot and labels the axes
plt.scatter(x,y)
plt.xlabel("Temperature °F")
plt.ylabel("Chirps per Minute")
plt.title("Cricket Chirps by Temperature")

# prints the correlation coefficient
print(f"Correlation between Temperature and Chirps/Min: {x.corr(y)}")

# show the plot
plt.show()