#!/usr/bin/env python3

import h5py
import numpy as np

with h5py.File('~/si486l/data/2d/sep3.h5') as f:
  for dataset in f:
    print(dataset)
    #print(f[dataset])
  #print(f['data'][2,:])
  #alldata=f['data'][:]
#print(alldata)
