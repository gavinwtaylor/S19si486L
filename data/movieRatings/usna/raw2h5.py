#!/usr/bin/env python3

import h5py
import csv
import numpy as np

data=np.zeros((700,34),dtype=int)

header=True
row=0
with open('usnaRaw.csv') as csvfile:
  reader=csv.reader(csvfile)
  for line in reader:
    if header:
      header=False
      continue
    if 'Faculty' in line[1]:
      data[row][0]=1
    if 'Male' in line[2]:
      data[row][1]=1
    for i in range(3,35):
      if line[i] is not '':
        data[row][i-1]=int(line[i])
    row=row+1

