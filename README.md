[![PyPI version](https://badge.fury.io/py/tadasets.svg)](https://badge.fury.io/py/tadasets)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tadasets)
[![Codecov](https://codecov.io/gh/scikit-tda/tadasets/branch/master/graph/badge.svg)](https://codecov.io/gh/scikit-tda/tadasets)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This package provides some nice utilities for creating and loading data sets
that are useful for Topological Data Analysis. Currently, we provide various
synthetic data sets with particular topological features.

# Setup

Installation is as easy as

```
pip install tadasets
```

# Usage

The shape constructors are exposed in a functional interface, each returning a numpy array containing data sampled on the object. Available objects include

- torus
- d-sphere
- swiss roll
- infinity sign
- eyeglasses

Each shape can be embedded in arbitrary ambient dimension by supplying the `ambient` argument. Additionally, noise can be added to the shape through the `noise` argument.

```python
import tadasets

torus = tadasets.torus(n=2000, c=2, a=1, ambient=200, noise=0.2)
swiss_roll = tadasets.swiss_roll(n=2000, r=4, ambient=10, noise=1.2)
dsphere = tadasets.dsphere(n=1000, d=12, r=3.14, ambient=14, noise=0.14)
infty_sign = tadasets.infty_sign(n=3000, noise=0.1)
eyeglasses = tadasets.eyeglasses(n=1000, r1=1, r2=2, neck_size=.5, noise=0.1, ambient=10)
```

## Contributions

We welcome contributions of all shapes and sizes. There are lots of opportunities for potential projects, so please get in touch if you would like to help out. Everything from an implementation of your favorite distance, notebooks, examples, and documentation are all equally valuable so please don’t feel you can’t contribute.

If you have ideas for new shapes or features, please do suggest them in an issue and submit a pull request!

To contribute please fork the project make your changes and submit a pull request. We will do our best to work through any issues with you and get your code merged into the main branch.
