#!/usr/bin/env python3

import numpy as np
import h5py
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

'''
Load the data from the HDF5 file
'''
with h5py.File(filename,'r') as f:
  ratings=f['ratings'][:]

(n,k)=ratings.shape
print(n,"respondants")

print(100*sum(ratings[:,1]==0)/n,'percent were female')

foods=ratings[:,2:20]
_,fk=foods.shape
movies=ratings[:,20:]
_,mk=movies.shape

print(100*np.sum(foods>0)/(n*fk),'percent of foods were rated')
print(100*np.sum(movies>0)/(n*mk),'percent of movies were rated')

xs,ys=np.where(foods>0)
s=0
for i in range(len(xs)):
  s=s+foods[xs[i],ys[i]]
print('average rating of foods was',s/(n*fk))
