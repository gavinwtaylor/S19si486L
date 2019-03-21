#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

def makeData(N,noise):
  xs=np.random.random(N)*2
  ys=np.sin(4*xs)+noise*np.random.randn(N)
  return xs,ys

def linearFeats(xs):
  Phi=np.array([[x] for x in xs])
  return Phi

def polyFeats(xs,degree):
  Phi=np.array([[pow(x,i) for i in range(1,degree+1)] for x in xs])
  return Phi

def RBFs(xs,centers,epsilon):
  Phi=np.array([[np.exp(-pow(epsilon*(x-xc),2)) for xc in centers] for x in xs])
  return Phi

def plotApprox(xs,ys,testXs,Phi,testPhi):
  n,k=Phi.shape
  plt.plot(xs,ys,'o')
  for i in range(k):
    plt.plot(testXs,testPhi[:,i],':')
  ridge=Ridge(alpha=0.01,normalize=True)
  ridge.fit(Phi,ys)
  testYs=ridge.predict(testPhi)
  plt.plot(testXs,testYs)
  plt.show()

xs,ys=makeData(10,.1)
testXs=np.linspace(0,2)

Phi=linearFeats(xs)
testPhi=linearFeats(testXs)
plotApprox(xs,ys,testXs,Phi,testPhi)

Phi=polyFeats(xs,3)
testPhi=polyFeats(testXs,3)
plotApprox(xs,ys,testXs,Phi,testPhi)

centers=[0,.5,1,1.5,2]
Phi=RBFs(xs,centers,1)
testPhi=RBFs(testXs,centers,1)
plotApprox(xs,ys,testXs,Phi,testPhi)
