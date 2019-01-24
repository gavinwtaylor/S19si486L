import numpy as np
import h5py
import argparse
import matplotlib.pyplot as plt
from math import sqrt

def calcError(A):
  n,k=A.shape
  errors=[]
  u,s,vh=np.linalg.svd(A)
  for i in range(0,k):
    s[k-i-1]=0
    Sigma=np.zeros((n,k))
    Sigma[:k,:]=np.diag(s)
    Ahat=u@Sigma@vh
    Atilde=A-Ahat
    err=0
    for row in range(n):
      for col in range(k):
        err=err+pow(Atilde[row,col],2)
    err=sqrt(err/(n*k))
    errors.append(err)
  errors.reverse()
  return errors[1:]


parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

'''
Load the data from the HDF5 file
'''
with h5py.File(filename,'r') as f:
  data=f['ratings'][:] #f['data'] doesn't actually load the data - f['data'][:]
                    #does
food=data[:,2:20]
movies=data[:,20:]

n,k=food.shape
indices=[]
for row in range(n):
  if sum(food[row,:]==0)==0:
    indices.append(row)
food=food[indices,:]

n,k=movies.shape
indices=[]
for row in range(n):
  if sum(movies[row,:]==0)==0:
    indices.append(row)
movies=movies[indices,:]

fdErr=calcError(food)
mvErr=calcError(movies)
plt.plot([x for x in range(1,len(fdErr)+1)],fdErr)
plt.plot([x for x in range(1,len(mvErr)+1)],mvErr)
plt.show()



'''
means=np.mean(data,axis=0)
means=np.tile(means,(n,1))
data=data-means
u,s,vh=np.linalg.svd(data)

usableS=.1*s

vh[0,:]=vh[0,:]*usableS[0]
vh[1,:]=vh[1,:]*usableS[1]

plt.plot(data[:,0],data[:,1],'.')
plt.plot([-vh[0,0],vh[0,0]],[-vh[0,1],vh[0,1]],linewidth=5)
plt.plot([-vh[1,0],vh[1,0]],[-vh[1,1],vh[1,1]])
plt.show()
'''
