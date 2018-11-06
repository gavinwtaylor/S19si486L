#!/usr/bin/env python3

import idx2numpy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pics=idx2numpy.convert_from_file('train-images-idx3-ubyte')
labels=idx2numpy.convert_from_file('train-labels-idx1-ubyte')
print(pics.shape,labels.shape)
indicesOfThrees=np.nonzero(labels==3)[0]
threes=pics[indicesOfThrees,:,:]
print(threes.shape)
shapenThrees=np.reshape(threes,(6131,784))
print(shapenThrees.shape)
u,s,vh=np.linalg.svd(shapenThrees)
keepK=10
s[keepK:]=np.zeros(784-keepK)
Sigma=np.zeros((6131,784))
Sigma[0:784,0:784]=np.diag(s)
print(u.shape,Sigma.shape,vh.shape)
shapenThrees=np.dot(np.dot(u,Sigma),vh)
threes=np.reshape(shapenThrees,(6131,28,28))
plt.imshow(threes[2,:,:],cmap='gray')
plt.show()
