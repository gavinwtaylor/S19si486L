#!/usr/bin/env python3

import numpy as np

a=np.array([[2,3,4],[3,4,5],[4,5,6]])
b=np.array([[1,0,1,0],[0,1,1,0],[1,1,0,1],[1,1,1,0]])
print(np.linalg.inv(b))
print(np.linalg.inv(a))
