#!/usr/bin/env python3

from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

lr = sys.argv[rank+1]
print("My learning rate is "+lr)
