#!/usr/bin/env python3

import numpy as np
import argparse
import matplotlib.pyplot as plt

base='/Users/taylor/si486l/data/movieRatings/usna/'
#base='/home/_scs/taylor/si486l/data/movieRatings/usna/'
#base='/home/scs/taylor/si486l/data/movieRatings/usna/'
foods=[]
with open(base+"features.txt") as f:
  f.readline()
  f.readline()
  for i in range(18):
    foods.append(f.readline().strip())

def getData(filename):
  import h5py
  with h5py.File(filename,'r') as f:
    data=f['ratings'][:]
    food=data[:,2:20]
    return food

def seeClusterDistance(data):
  from sklearn import cluster
  clusters=[]
  distance=[]

  '''
  normData=np.zeros(data.shape)
  n,k=data.shape
  normData[:]=data[:]
  stds=np.std(normData,axis=0)
  for i in range(k):
    normData[:,i]=(1/stds[i])*normData[:,i]
  '''

  for i in range(2,100):
    km=cluster.KMeans(n_clusters=i)
    km.fit(data)
    clusters.append(i)
    distance.append(km.inertia_)
  plt.plot(clusters,distance)
  plt.show()

def seeClusters(data,k):
  from sklearn import cluster
  normData=np.zeros(data.shape)
  n,feats=data.shape

  '''
  normData[:]=data[:]
  stds=np.std(normData,axis=0)
  for i in range(k):
    normData[:,i]=(1/stds[i])*normData[:,i]
  '''

  km=cluster.KMeans(n_clusters=k,n_init=20)
  km.fit(data)
  nums=[]
  for i in range(k):
    nums.append(sum(km.labels_==i))
  index=np.argsort(nums)
  means=np.mean(data,axis=0)
  plt.plot(km.cluster_centers_[index[-1]]-means,'-o')
  plt.plot(km.cluster_centers_[index[-2]]-means,'-o')
  plt.legend(["biggest","2nd-biggest"])
  print([(i,foods[i]) for i in range(len(foods))])
  plt.show()

def seeSingularValues(data):
  n,_=data.shape
  means=np.mean(data,axis=0)
  means=np.tile(means,(n,1))
  data=data-means
  u,s,vt=np.linalg.svd(data)
  plt.plot(s)
  plt.show()

def seeSingularVectors(data):
  n,_=data.shape
  means=np.mean(data,axis=0)
  means=np.tile(means,(n,1))
  data=data-means
  u,s,vt=np.linalg.svd(data)
  plt.plot(vt[0,:],'-o')
  plt.plot(vt[1,:],'-o')
  plt.legend(["first","second"])
  print([(i,foods[i]) for i in range(len(foods))])
  plt.show()

data=getData(base+"usna.h5")
seeClusterDistance(data)
seeClusters(data,30)
seeSingularValues(data)
seeSingularVectors(data)
