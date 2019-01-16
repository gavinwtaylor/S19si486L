import h5py
import numpy as np
from scipy import sparse

def readCSR(filename):
  with h5py.File(filename,'r') as h5F:
    grp=h5F['csr']
    A=sparse.csr_matrix((grp['data'][:],grp['indices'][:],
      grp['indptr'][:]),grp.attrs['shape'])
    return A

A=readCSR('nytimes.h5')
print(A.shape)
