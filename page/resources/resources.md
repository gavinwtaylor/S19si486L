#Resources

###Books

- (LFD) Abu-Mostafa, Magdon-Ismail, and Lin. __Learning From Data__.
- (ISL) [James, Witten, Hastie, and Tibshirani.  __An Introduction to
  Statistical Learning__](JWHT.pdf). (generously provided for free by the
  authors)
- (ESL) [Hastie, Tibshirani, and Friedman.  __The Elements of Statistical
  Learning__](ESL.pdf). (generously provided for free by the authors)
- \(MML\) [Deisenroth, Faisal, and Ong.  __Mathematics for Machine
  Learning__](https://mml-book.github.io/). (generously provided for free by
  the authors)

###Software Libraries

- [Numpy](http://www.numpy.org/)
- [Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html)
- [HDF5 for Python](https://www.h5py.org/)

###Setting up a Python Virtual Environment

Virtual environments are useful for setting up your Python libraries without
impacting the whole system's Python installation (or when you don't have root
access).  To build an environment for Python 3 called `mypy3`, and install
some libraries, run the following commands:
```
python3 -m virtualenv mypy3
source mypy3/bin/activate
pip install numpy scipy h5py matplotlib
```

While the virtual environment is active, all calls to python, pip, etc. will
be handled by the installation set up for that virtual environment.  To leave
it, run `deactivate`.  You'll probably want an alias set up to activate your
favorite virtual environment.
