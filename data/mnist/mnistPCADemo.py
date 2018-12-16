#!/usr/bin/env python3

import idx2numpy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import sys

pics=idx2numpy.convert_from_file('train-images-idx3-ubyte')
labels=idx2numpy.convert_from_file('train-labels-idx1-ubyte')
print(pics.shape,labels.shape)

indicesOfThrees=np.nonzero(labels==3)[0]
threes=pics[indicesOfThrees,:,:]
print(threes.shape)

shapenThrees=np.reshape(threes,(6131,784))
print(shapenThrees.shape)

pca=PCA()
pca.fit(shapenThrees)
print(pca.components_.shape)
components=np.reshape(pca.components_,(784,28,28))
print(components[0,:,:])

'''
threes=np.reshape(shapenThrees,(6131,28,28))
plt.imshow(threes[0,:,:],cmap='gray')
plt.show()
plt.imshow(threes[1,:,:],cmap='gray')
plt.show()
plt.imshow(threes[2,:,:],cmap='gray')
plt.show()
'''
