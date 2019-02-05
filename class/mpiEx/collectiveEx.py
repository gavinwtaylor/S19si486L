#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

theArray=np.zeros((3,))
if rank==0:
  theArray[0]=10
  theArray[1]=11
  theArray[2]=12
theArray=comm.bcast(theArray,root=0)
print("Rank %d has array %s" % (rank,str(theArray)))

theArray=np.random.random((3,))
theArray=comm.gather(theArray,root=0)
print("Rank %d has array %s" % (rank,str(theArray)))

#Do a whole lot of work, get some accuracy
accuracy=np.random.random((1,))
print("Rank %d has accuracy %s" % (rank,str(accuracy)))
if rank==0:
  minAcc=np.zeros((1,))
  comm.Reduce(accuracy,minAcc,op=MPI.MAX,root=0)
  print("maximum accuracy is %s" % (str(minAcc)))
else:
  comm.Reduce(accuracy,None,op=MPI.MAX,root=0)



