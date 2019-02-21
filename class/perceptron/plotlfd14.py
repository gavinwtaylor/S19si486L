#!/usr/bin/env python3

import h5py,argparse
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

parser=argparse.ArgumentParser()
parser.add_argument("filename",help="file to read and plot")
filename=parser.parse_args().filename

with h5py.File(filename,'r') as f:
  Ns=f['Ns'][:]
  ds=f['ds'][:]
  vals=f['vals'][:]

vals=vals.T
fig=plt.figure()
ax=Axes3D(fig)

Ns,ds=np.meshgrid(Ns,ds)

ax.plot_surface(Ns,ds,vals,cmap=cm.coolwarm)
ax.set_xlabel('N')
ax.set_ylabel('dimensions')
ax.set_zlabel('average # of epochs')
plt.show()
