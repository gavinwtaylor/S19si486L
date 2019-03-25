from scipy.io import arff
import numpy as np
import h5py

allData=[]
for i in range(1,6):
  with open("/home/scs/taylor/faculty/si486l/data/polishBankruptcy/%dyear.arff"%i) as f:
    data,meta=arff.loadarff(f)
    data=np.array([[x for x in line] for line in data])
    n,k=data.shape
    data=np.concatenate((i*np.ones((n,1)),data),axis=1)
    allData.append(data)
data=np.concatenate(allData)

clean=[]
messy=[]
n,k=data.shape
for row in range(n):
  if sum(sum(np.where(data[row,:]==b'nan')))==0:
    clean.append(row)
  else:
    messy.append(row)

np.random.shuffle(clean)
print(len(clean),len(messy))
messy.extend(clean[4000:])
clean=clean[:4000]
clean.sort()
messy.sort()

clean=data[clean,:]
messy=data[messy,:]

clean=clean.astype(float)
messy=messy.astype(float)

with h5py.File('training.h5','w') as f:
  dset=f.create_dataset('data',messy.shape,messy.dtype)
  dset[:]=messy[:]
with h5py.File('validation.h5','w') as f:
  dset=f.create_dataset('data',clean.shape,clean.dtype)
  dset[:]=clean[:]
