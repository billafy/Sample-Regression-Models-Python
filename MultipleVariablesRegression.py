import pandas
from sklearn import linear_model as lm 
import matplotlib.pyplot as mpl
import numpy as np

df = pandas.read_csv("cars.csv") # pandas read_csv reads the dataset

x = df[["Volume","Weight"]] # x will take all the variables
y = df["CO2"] # y will take the output

multiReg = lm.LinearRegression() # creating a regression model
multiReg.fit(x,y) # fitting x and y into it

vol = input("Car's volume(in ccm) : ")
vol = int(vol)
wt = input("Car's weight(in kg) : ")
wt = int(wt)

CO2 = multiReg.predict([[vol,wt]]) # predict by passing the needed values
CO2 = np.around(float(CO2),2)

print("\nThe carbon dioxide emission of your car is",CO2,"grams")
