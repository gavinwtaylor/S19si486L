#!/usr/bin/env python3

import numpy as np

a=np.ones((4,3))
a[0,2]=0;
print(a)
a[1,1]=2;
print(a)
print(a[:,1])
print(a.shape)
