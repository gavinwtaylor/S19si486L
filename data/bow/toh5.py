import numpy as np
import csv
from scipy import sparse
import h5py

with open('docword.nytimes.txt') as f:
  n=int(f.readline().strip())
  k=int(f.readline().strip())
  A=sparse.lil_matrix((n,k))
  f.readline()
  count=0
  for line in f:
    line=line.split()
    for i in range(3):
      line[i]=int(line[i])
    A[line[0]-1,line[1]-1]=line[2]
    count=count+1
  A=sparse.csr_matrix(A)
  with h5py.File('nytimes.h5','a') as h5F:
    grp=h5F.create_group('csr')
    grp.create_dataset('data',data=A.data)
    grp.create_dataset('indptr',data=A.indptr)
    grp.create_dataset('indices',data=A.indices)
    grp.attrs['shape']=A.shape

