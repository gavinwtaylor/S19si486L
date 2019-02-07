#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

theArray=np.empty((3,))
if rank==0:
  theArray[0]=10
  theArray[1]=11
  theArray[2]=12
print("BCAST BEFORE: Rank %d has array %s" % (rank,str(theArray)))
comm.Bcast(theArray,root=0)
print("BCAST AFTER: Rank %d has array %s" % (rank,str(theArray)))

comm.Barrier()

theArray=np.random.random((3,))
print("GATHER BEFORE: Rank %d has array %s" % (rank,str(theArray)))
if rank==0:
  result=np.empty((size,3))
  comm.Gather(theArray,result,root=0)
  print("GATHER AFTER: Rank %d gathered %s" % (rank,str(result)))
else:
  comm.Gather(theArray,None,root=0)

comm.Barrier()

#Pretend we've just done a whole lot of work, and have calculated 
#some accuracy
accuracy=np.random.random((1,))
print("REDUCE BEFORE: Rank %d has accuracy %s" % (rank,str(accuracy)))
if rank==0:
  maxAcc=np.empty((1,))
  comm.Reduce(accuracy,maxAcc,op=MPI.MAX,root=0)
  print("REDUCE AFTER: maximum accuracy is %s" % (str(maxAcc)))
else:
  comm.Reduce(accuracy,None,op=MPI.MAX,root=0)

comm.Barrier()

accuracy=np.random.random((1,))
print("ALLREDUCE BEFORE: Rank %d has accuracy %s" % (rank,str(accuracy)))
maxAcc=np.empty((1,))
comm.Allreduce(accuracy,maxAcc,op=MPI.MAX)
print("ALLREDUCE AFTER: maximum accuracy is %s" % (str(maxAcc)))
if maxAcc==accuracy:
  print("That's me!  Rank %d is best!" % rank)
