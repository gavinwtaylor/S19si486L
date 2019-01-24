import numpy as np
import h5py
import argparse
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

'''
Load the data from the HDF5 file
'''
with h5py.File(filename,'r') as f:
  data=f['data'][:] #f['data'] doesn't actually load the data - f['data'][:]
                    #does
n,_=data.shape

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

'''another way of calling PCA without centering your data first
pca=PCA(n_components=1)
pca.fit(data)
print(pca.components_)
'''
