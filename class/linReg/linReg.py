#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import argparse
from mpl_toolkits.mplot3d import Axes3D

'''
Generate N 2d datapoints, plus noise
'''
def genData1d(N,noise=1):
  line=np.random.randn(2) #random A,B for Ax+B=y
  xs=np.random.random(N)*20-10 #random points on x-axis between -10 and 10

  #for each of those points, calculate x,and 1
  data=np.asarray( [[x,1] for x in xs] )
  ys=data@line #calculate resulting y value
  
  #for each, add some random error
  ys=ys+noise*np.random.randn(N)

  return xs,ys

'''
Generate N 3d datapoints, plus noise
'''
def genData2d(N,noise=1):
  line=np.random.randn(3) #random A,B for Ax_1+Bx_2+C=y
  xs=np.random.random((N,2))*20-10 #random points (-10,-10) and (10,10)

  #for each of those points, calculate x,and 1
  data=np.asarray( [[x[0],x[1],1] for x in xs] )
  ys=data@line #calculate resulting y value
  
  #for each, add some random error
  ys=ys+noise*np.random.randn(N)

  return xs,ys

'''
Calculate the line of best fit in x,y space.
'''
def plotItLin(xs,ys,w):
  plt.plot(xs,ys,'.')
  plt.plot([-10,10],np.array([[-10,1],[10, 1]])@w)
  plt.show()

'''
Fancy-shmancy drawing of points and plane of best fit in x,x^2 space
'''
def plot3D(data,ys,w=None):
  fig=plt.figure()
  ax=Axes3D(fig)
  ax.set_xlim(-10,10)
  ax.set_ylim(-10,10)
  if w is not None:
    X1=np.arange(-10,10)
    X2=np.arange(-10,10)
    plane=np.asarray([[x1,x2,1] for x1 in X1 for x2 in X2])@w
    plane=plane.reshape((20,20))
    X1,X2=np.meshgrid(X1,X2)
    ax.plot_surface(X1,X2,plane,color="lightgray",shade=False,\
        alpha=.7)
  ax.scatter(data[:,1],data[:,0],ys)
  ax.set_xlabel('$x_1$')
  ax.set_ylabel('$x_2$')
  ax.set_zlabel('$y$')
  plt.show()

def plotPoints(xs,ys):
  plt.plot(xs,ys,'.')
  plt.show()

'''
Do linear regression
'''
def linReg(data,ys):
  w=np.linalg.pinv(data)@ys
  return w

parser=argparse.ArgumentParser()
parser.add_argument("--N",type=int,\
    help="Number of datapoints to generate",default=20)
parser.add_argument("--noise",type=float,\
    help="amount of noise",default=.5)
args=parser.parse_args()

N=args.N
noise=args.noise

xs,ys=genData1d(N,noise=noise)
plotPoints(xs,ys)

data=np.ones((N,2))
data[:,0]=xs
w=linReg(data,ys)
plotItLin(xs,ys,w)

xs,ys=genData2d(N,noise=noise)
data=np.ones((N,3))
data[:,:2]=xs
plot3D(data,ys)
w=linReg(data,ys)
plot3D(data,ys,w)
