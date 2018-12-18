#!/usr/bin/env python3

import numpy as np
import h5py
import argparse
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("--onecolor",action="store_true")
args=parser.parse_args()
filename=args.filename

with h5py.File(filename,'r') as f:
  data=f['data'][:]
  targets=f['targets'][:]

if args.onecolor:
  plt.plot(data[:,0],data[:,1],'.')
else:
  for row in range(len(data)):
    plt.plot(data[row,0],data[row,1],'.',color='C'+str(int(targets[row])))
plt.show()
