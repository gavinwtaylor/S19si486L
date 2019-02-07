#!/usr/bin/env python3

from mpi4py import MPI
import sys,socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(str(size)+' '+str(rank)+' '+socket.gethostname())
