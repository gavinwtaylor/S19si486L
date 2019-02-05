#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank!=0:
  data=np.random.random((3,))
  comm.Send(data,dest=0,tag=0)
else:
  for otherRank in range(1,size):
    r=np.zeros((3,))
    comm.Recv(r,source=otherRank,tag=0)
    print(r)
