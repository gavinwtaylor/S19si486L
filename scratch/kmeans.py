#!/usr/bin/env python3
#import idx2numpy
import argparse
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import h5py

def drawIt(data,centroids,assign):
  for row in range(len(data)):
    plt.plot(data[row,0],data[row,1],'.',color='C'+str(int(assign[row])))
  for c in centroids:
    plt.plot(c[0],c[1],'o')
  plt.show()

def kmeans(data,k):
  (n,m)=data.shape
  centroids=data[np.random.permutation(n)[:k],:]
  run=True
  count=0
  assign=np.zeros(n,dtype=int)
  while run:
    print(centroids)
    run=False
    print(count)
    count=count+1
    for i in range(n):
      mindist=float('inf')
      minind=0
      for c in range(k):
        dist=np.linalg.norm(data[i,:]-centroids[c,:])
        if dist<mindist:
          mindist=dist
          minind=c
      if minind!=assign[i]:
        assign[i]=minind
        run=True
    drawIt(data,centroids,assign)
    for c in range(k):
      centroids[c,:]=np.mean(data[np.where(assign==c)[0],:],0)
  totalDist=0
  for i in range(n):
    totalDist=totalDist+sqrt(np.linalg.norm(data[i,:]-\
        centroids[assign[i],:]))
  return (centroids,totalDist/n,assign)

#pics=idx2numpy.convert_from_file('../data/mnist/train-images-idx3-ubyte')
#shaped=np.reshape(pics,(60000,784))

parser=argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("k",type=int)
args=parser.parse_args()
filename=args.filename

with h5py.File(filename,'r') as f:
  data=f['data'][:]

centroids,avgDist,assign=kmeans(data,args.k)
drawIt(data,centroids,assign)
