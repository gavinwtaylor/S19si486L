import numpy as np
import h5py
import argparse
from math import pow,sqrt

alpha=.01

def SGD(data,locs,k):
  n,m=data.shape
  p=np.random.normal(0,.1,(n,k))
  q=np.random.normal(0,.1,(k,m))
  np.random.shuffle(locs)
  nLocs=len(locs)
  testLocs=locs[:int(.1*nLocs)]
  trainLocs=locs[int(.1*nLocs):]

  for epoch in range(1000):
    np.random.shuffle(trainLocs)
    for loc in trainLocs:
      i,j=loc
      err=data[i,j]-np.dot(p[i,:],q[:,j])
      p[i,:]=p[i,:]+alpha*err*q[:,j]
      q[:,j]=q[:,j]+alpha*err*p[i,:]
    totErr=0
    trainTotErr=0
    predData=np.dot(p,q)
    for loc in testLocs:
      i,j=loc
      totErr=totErr+pow(data[i,j]-predData[i,j],2)
    for loc in trainLocs:
      i,j=loc
      trainTotErr=totErr+pow(data[i,j]-predData[i,j],2)
      print(' ',data[i,j],predData[i,j])
    print(sqrt(trainTotErr/len(trainLocs)),sqrt(totErr)/len(testLocs))


parser=argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("numFeats",type=int)
args=parser.parse_args()
filename=args.filename
k=args.numFeats

with h5py.File(filename,'r') as f:
  data=f['ratings'][:]

n,m=data.shape

ratingLocs=[]
for i in range(n):
  for j in range(m):
    if data[i,j]!=0:
      ratingLocs.append((i,j))

SGD(data,ratingLocs,k)
