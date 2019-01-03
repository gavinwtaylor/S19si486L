#!/usr/bin/env python3

import numpy as np
import h5py
import argparse

'''
Actually generate the data with the given mean and covariance
'''
def makeData(mean,cov,n):
  newdata=np.random.multivariate_normal(mean,cov,size=n)
  return newdata

'''
Shuffle the data and targets the same way, so they stay aligned
'''
def unisonShuffle(a,b):
  n=a.shape[0]
  p=np.random.permutation(n)
  return a[p],b[p]

'''
Make a random mean and covariance
'''
def randomParams(dims):
  means=20*np.random.rand(dims)-10*np.ones(2)
  cov=np.random.random((dims,dims))
  cov=np.dot(cov,cov.T)
  return means,cov


parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

N=25 #hardcoded... gross
means=[]
covs=[]
Ns=[]
for i in range(10): #10 clusters... again, gross
  mean,cov=randomParams(2)
  means.append(mean)
  covs.append(cov)
  Ns.append(N)

data=np.zeros((sum(Ns),len(means[0])))
targets=np.zeros(sum(Ns),dtype=int)

for i in range(len(Ns)):
  data[sum(Ns[:i]):sum(Ns[:i+1])]=\
      np.random.multivariate_normal(means[i],covs[i],size=Ns[i])
  targets[sum(Ns[:i]):sum(Ns[:i+1])]=i*np.ones(Ns[i],dtype=int)

(data,targets)=unisonShuffle(data,targets)

'''
store the data into an HDF5 file
'''
with h5py.File(filename,'w') as f:
  dset=f.create_dataset('data',data.shape,data.dtype)
  dset[:]=data[:]
  tset=f.create_dataset('targets',targets.shape,targets.dtype)
  tset[:]=targets[:]
