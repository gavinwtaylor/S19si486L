#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

print("Displaying a cubic y=Ax^3+Bx^2+Cx+D")

coeffs=np.zeros((4,1))
coeffs[0]=float(input("A? "))
coeffs[1]=float(input("B? "))
coeffs[2]=float(input("C? "))
coeffs[3]=float(input("D? "))

xs=np.linspace(-10,10,100)#get 100 points, evenly spaced between -10 and 10

vals=np.ones((100,4))
vals[:,0]=xs*xs*xs  #x^3 for all values of x (remember, * is piecewise
                    #multiplication)
vals[:,1]=xs*xs #x^2
vals[:,2]=xs
#leave the 3th column as all ones

ys=vals@coeffs

plt.plot(xs,ys)
plt.show()
