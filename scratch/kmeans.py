#!/usr/bin/env python3
import idx2numpy
import numpy as np
import matplotlib.pyplot as plt

def kmeans(data,k):
  (n,m)=data.shape
  centroids=data[np.random.permutation(n)[:k],:]
  run=True
  count=0
  assign=np.zeros(n)
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
    for c in range(k):
      centroids[c,:]=np.mean(data[np.where(assign==c)[0],:],0)
      print(c,np.where(assign==c)[0].shape)

pics=idx2numpy.convert_from_file('../data/mnist/train-images-idx3-ubyte')
shaped=np.reshape(pics,(60000,784))
#shaped=np.random.multivariate_normal(np.array([2,2]),np.array([[1,0],[0,1]]),size=5)
#shaped=np.concatenate((shaped,np.random.multivariate_normal(np.array([-2,-2]),np.array([[1,0],[0,1]]),size=7)))
#print(shaped)
kmeans(shaped,2)
