import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values
# x = x.reshape(-1,1)
# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.20)
print(xtrain)
# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)
print(xtrain)
# Create the model
model = LinearRegression().fit(xtrain, ytrain)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_[0]),2)
intercept = round(float(model.intercept_),2)

# Print out the linear equation and r squared value:
print("y=", coef, "x +", intercept)

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array

# get the predicted y values for the xtest values - returns an array of the results

# round the value in the np array to 2 decimal places


# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
plt.figure(figsize=(5,4))
plt.plot(x, coef*x + intercept, c="b", label="line of best fit")

plt.legend()
plt.show()