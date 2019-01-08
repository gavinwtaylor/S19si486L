#!/usr/bin/env python3

import numpy as np
import h5py
import argparse
import csv

def parseMovies(directory):
  movies=[]
  movieMap=dict()
  with open(directory+'/movies.csv') as csvfile:
    reader=csv.reader(csvfile)
    first=True
    for row in reader:
      if first:
        first=False
      else:
        movieMap[int(row[0])]=len(movies)
        movies.append(row[1])
  return movies,movieMap

def parseRatings(directory,movieMap):
  last=0
  with open(directory+'/ratings.csv') as csvfile:
    reader=csv.reader(csvfile)
    first=True
    for row in reader:
      if first:
        first=False
      else:
        if int(row[0])>last:
          last=int(row[0])
  ratings=np.zeros((last,len(movies)),dtype=int)
  with open(directory+'/ratings.csv') as csvfile:
    reader=csv.reader(csvfile)
    first=True
    for row in reader:
      if first:
        first=False
      else:
        user=int(row[0])-1
        movie=movieMap[int(row[1])]
        ratings[user,movie]=int(float(row[2]))
  return ratings

parser=argparse.ArgumentParser()
parser.add_argument("directory")
args=parser.parse_args()
directory=args.directory

movies,movieMap=parseMovies(directory)
ratings=parseRatings(directory,movieMap)

with h5py.File(directory+'/'+directory+'.h5') as f:
  ratingsSet=f.create_dataset('ratings',ratings.shape,ratings.dtype)
  ratingsSet[:]=ratings[:]
