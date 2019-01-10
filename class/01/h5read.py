#!/usr/bin/env python3

import h5py
import numpy as np
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("filename")
args=parser.parse_args()
filename=args.filename

with h5py.File(filename) as f:
  for dataset in f:
    print(dataset)
    #print(f[dataset])
  #print(f['data'][2,:])
  #alldata=f['data'][:]
#print(alldata)
