#!/usr/bin/env python3

import numpy as np

#1
A=np.array([[1,2],[4,5],[7,8]])
B=np.array([[1,1,0],[0,1,1],[1,0,1]])
#print(A@B)

#2
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,1,0],[0,1,1],[1,0,1]])
print(A@B)

#3
print(B@A)

#4
A=np.array([[1,2,1,2],[4,1,-1,-4]])
B=np.array([[0,3],[1,-1],[2,1],[5,2]])
print(A@B)

#5
print(B@A)
