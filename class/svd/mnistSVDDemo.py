#!/usr/bin/env python3

import idx2numpy
import numpy as np
import matplotlib.pyplot as plt
import argparse

def showNums(data):
  plt.subplot(3,1,1)
  plt.imshow(data[0,:,:],cmap='gray')
  plt.subplot(3,1,2)
  plt.imshow(data[1,:,:],cmap='gray')
  plt.subplot(3,1,3)
  plt.imshow(data[2,:,:],cmap='gray')
  plt.show()

def showReconstruct(data,rebuild):
  plt.subplot(3,2,1)
  plt.imshow(data[0,:,:],cmap='gray')
  plt.subplot(3,2,3)
  plt.imshow(data[1,:,:],cmap='gray')
  plt.subplot(3,2,5)
  plt.imshow(data[2,:,:],cmap='gray')
  plt.subplot(3,2,2)
  plt.imshow(rebuild[0,:,:],cmap='gray')
  plt.subplot(3,2,4)
  plt.imshow(rebuild[1,:,:],cmap='gray')
  plt.subplot(3,2,6)
  plt.imshow(rebuild[2,:,:],cmap='gray')
  plt.show()
parser=argparse.ArgumentParser()
parser.add_argument("mnistDirectory")
parser.add_argument("--keepK",type=int)
args=parser.parse_args()

pics=idx2numpy.convert_from_file(args.mnistDirectory+'/train-images-idx3-ubyte')
labels=idx2numpy.convert_from_file(args.mnistDirectory+'/train-labels-idx1-ubyte')
print(pics.shape,labels.shape)
showNums(pics)

############

indicesOfThrees=np.nonzero(labels==3)[0]
threes=pics[indicesOfThrees,:,:]
print(threes.shape)
numThrees=threes.shape[0]
showNums(threes)

shapenThrees=np.reshape(threes,(numThrees,784))
print(shapenThrees.shape)

############

u,s,vh=np.linalg.svd(shapenThrees)

plt.plot(s)
#plt.ylim((-5,100))
plt.show()

############

keepK=args.keepK
s[keepK:]=np.zeros(784-keepK)
Sigma=np.zeros((numThrees,784))
Sigma[0:784,0:784]=np.diag(s)
print(u.shape,Sigma.shape,vh.shape)

shapenThrees=u@Sigma@vh
newThrees=np.reshape(shapenThrees,(numThrees,28,28))
showReconstruct(threes,newThrees)
