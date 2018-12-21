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

- [Numpy](http://www.numpy.org/): linear algebra
- [Scipy](http://scipy.github.io/devdocs/): algorithms and data structures for
  scientific computing
- [Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html): for
  making plots and graphs
- [HDF5 for Python](https://www.h5py.org/): high-density data storage format
- [argparse](https://docs.python.org/3/howto/argparse.html): handles
  command-line arguments cleaner than sys.argv

###Setting up a Python Virtual Environment

Virtual environments are useful for setting up your Python libraries without
impacting the whole system's Python installation (or when you don't have root
access).  To build an environment for Python 3 and install
some libraries, run the following commands from the home directory:
```
python3 -m virtualenv <someName>
source <someName>/bin/activate
pip install numpy scipy h5py matplotlib
```

While the virtual environment is active, all calls to python, pip, etc. will
be handled by the installation set up for that virtual environment.  To leave
it, run `deactivate`.  You'll probably want an alias set up to activate your
favorite virtual environment.
