import numpy as np # Python Library used for efficient computation on arrays
import scipy as sp # Science Python basically
from scipy import stats # Importing stats module from scipy
import matplotlib.pyplot as mpl # Matrices and Graph Plot Library called to plot our graph

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # random sample dataset 
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope,intercept,r,p,std_err = stats.linregress(x,y) # passing our dataset (x,y) to linear regression function in stats
                                                    # module to get the slope, x and y intercepts, r(correlation),
                                                    # p(P value of Regression), std_err(Standard Error of Regression)    

def predictSpeed(x) : # this function will predict the speed of our car i.e. predict y value on given x value
    return (slope*x) + intercept # this formula is basically y = a + bx (a : intercept, b : slope)

mymodel = list(map(predictSpeed,x)) # this will map our function predictSpeed values to a Python List (we named it mymodel) 

mpl.scatter(x,y) # scatter the x and y points on the graph
mpl.plot(x,mymodel) # plot mymodel
mpl.show() # show it 

yrs = input("How old is your car : ") # take input of age of the car
yrs = float(yrs)
speed = predictSpeed(yrs) # pass it to the function

print("The speed of your car is :",np.around(speed,3)) # output our prediction

# Bawal Billa








