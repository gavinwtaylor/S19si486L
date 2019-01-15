#!/usr/bin/env python3

import numpy as np
import h5py
import matplotlib.pyplot as plt
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

'''
Load the data from the HDF5 file
'''
with h5py.File(filename,'r') as f:
  ratings=f['ratings'][:,1:]

(n,k)=ratings.shape

malerows=np.where(ratings[:,0]>0)[0]
fmrows=np.where(ratings[:,0]==0)[0]

male=ratings[malerows,:]
female=ratings[fmrows,:]

mRatings=[]
fRatings=[]
for i in range(1,6):
  mRatings.append(sum(sum(male==i)))
  fRatings.append(sum(sum(female==i)))

xs=[i for i in range(1,6)]
plt.plot(xs,mRatings,xs,fRatings)
plt.show()
