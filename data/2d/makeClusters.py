#!/usr/bin/env python3

import numpy as np
import h5py
import argparse

def makeData(mean,cov,n):
  newdata=np.random.multivariate_normal(mean,cov,size=n)
  if dataTarget:
    (data,target)=dataTarget
    newTarget=np.ones(n)
    return np.concatenate((data,newdata))
  return newdata

def unisonShuffle(a,b):
  n=a.shape[0]
  p=np.random.permutation(n)
  return a[p],b[p]

parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

N=25
means=[]
covs=[]
Ns=[]
means.append([-2,2])
covs.append([[.25,0],[0,.75]])
Ns.append(N)
means.append([2,2])
covs.append([[.75,0],[0,.75]])
Ns.append(N)
means.append([-2,-2])
covs.append([[.75,0],[0,.75]])
Ns.append(N)

data=np.zeros((sum(Ns),len(means[0])))
targets=np.zeros(sum(Ns),dtype=int)

for i in range(len(Ns)):
  data[sum(Ns[:i]):sum(Ns[:i+1])]=\
      np.random.multivariate_normal(means[i],covs[i],size=Ns[i])
  targets[sum(Ns[:i]):sum(Ns[:i+1])]=i*np.ones(Ns[i],dtype=int)

(data,targets)=unisonShuffle(data,targets)

with h5py.File(filename,'w') as f:
  dset=f.create_dataset('data',data.shape,data.dtype)
  dset[:]=data[:]
  tset=f.create_dataset('targets',targets.shape,targets.dtype)
  tset[:]=targets[:]
