import numpy as np
from numpy import random as rd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as mpl

age = [9,19,29,39,49,59,69,79,89,99]
fatal = [2,0,8,49,224,918,2727,7291,10241,3755]

model = np.poly1d(np.polyfit(age,fatal,2))

line = np.linspace(1,99)

mpl.scatter(age,fatal)
mpl.plot(line,model(line))
mpl.show()

pAge = input("Enter your age : ")
pAge = int(pAge)

if pAge <= 0 :
    print("Invalid age")
else : 
    fatalRate = (model(pAge)*100)/np.sum(fatal)

    if fatalRate < 0 : 
        fatalRate+=7

    print("Fatality rate :",np.around(fatalRate,2),"%")
