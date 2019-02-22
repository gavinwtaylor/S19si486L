#!/usr/bin/env python3

import numpy as np
import argparse,h5py
from mpi4py import MPI
from numba import jit

def genData(N,d):
  data=(np.random.random((N,d+1))*20)-10
  data[:,-1]=np.ones(N)

  line=np.random.randn(d+1)

  vals=data@line
  targets=(vals>0).astype(int)*2-1

  return data,targets,line

@jit(nopython=True)
def isMisclassified(pt,w,t):
  return t*pt@w<0

@jit(nopython=True)
def update(pt,w,t):
  w=w+t*pt
  return w

@jit
def learnOne(N,d):
  data,targets,f=genData(N,d)
  w=np.random.randn(d+1)

  epochs=0

  somewrong=True
  while somewrong:
    epochs=epochs+1
    somewrong=False
    for i in range(N):
      if isMisclassified(data[i,:],w,targets[i]):
        somewrong=True
        w=update(data[i,:],w,targets[i])
  return epochs

def getAvg(N,d,numIter=100):
  epochs=[]
  for i in range(numIter):
    epochs.append(learnOne(N,d))
  return sum(epochs)/numIter

def saveResults(Ns,ds,results,filename):
  vals=np.empty((len(Ns),len(ds)))

  for result in results:
    for r in result:
      N=Ns.index(r[0])
      d=ds.index(r[1])
      vals[N,d]=r[2]
  Ns=np.asarray(Ns)
  ds=np.asarray(ds)
  vals=np.asarray(vals)
  with h5py.File(filename,'w') as f:
    dset=f.create_dataset('Ns',Ns.shape,Ns.dtype)
    dset[:]=Ns[:]
    dset=f.create_dataset('ds',ds.shape,ds.dtype)
    dset[:]=ds[:]
    dset=f.create_dataset('vals',vals.shape,vals.dtype)
    dset[:]=vals[:]


parser=argparse.ArgumentParser()
parser.add_argument("filename",help="file to save results to")
filename=parser.parse_args().filename

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
Ns=[10*x for x in range(1,101)] #all values of N
ds=[x for x in range(2,21)] #all values of d

if rank==0:
  Nds=[(N,d) for d in ds for N in Ns] #(N,d) for all pairs of N and d
  scat=[[] for i in range(size)] #list of lists, one for each MPI process
  for i in range(len(Nds)):
    scat[i%size].append(Nds[i]) #populate the lists with (N,d) pairs, so
                                #each list has about the same number of pairs
  Nds=scat
else:
  Nds=None
Nds=comm.scatter(Nds,root=0) #distribute those lists to their appropriate process. Nds[0] goes to rank 0, Nds[1] goes to rank 1, etc.
results=[]
for Nd in Nds: #for this process's N,d pairs,
  N,d=Nd
  results.append((N,d,getAvg(N,d))) #calculate the average number of iterations, and store to a tuple, (N,d,iterations)

#at this point, every process has a list 'results' which contains the
#(N,d,iterations) tuple for its assigned set of N,d pairs. They all need
#to be gathered into one place
results=comm.gather(results,root=0) #this sends them all to the rank 0 process
if rank==0:
  saveResults(Ns,ds,results,filename) #store them all as an array
