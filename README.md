[![PyPI version](https://badge.fury.io/py/tadasets.svg)](https://badge.fury.io/py/tadasets)
[![Build Status](https://travis-ci.org/scikit-tda/tadasets.svg?branch=master)](https://travis-ci.org/scikit-tda/tadasets)
[![Codecov](https://codecov.io/gh/scikit-tda/tadasets/branch/master/graph/badge.svg)](https://codecov.io/gh/scikit-tda/tadasets)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# TaDAsets
Data sets apt for Topological Data Analysis. This project is a part of scikit-tda.

## Motivation

At SoCG 2018, there was discussion about the need for data sets for two main purposes
- Benchmarking new algorithms
- Demonstrating benefits of TDA

## Data generation

We provide constructors for some synthetic data sets that are popular in development and testing of TDA techniques.

* Torus
* Klein Bottle
* Swiss Roll

## Setup and Usage

You can install from Pypi
```
pip install tadasets
```

or from source

```
git clone https://github.com/scikit-tda/tadasets
cd tadasets
pip install -e .
```

Examples of usage is

```
import tadasets
data = tadasets.sphere(n=1000, r=10)
tadasets.plot3d(data)
```

or 

```
import tadasets
data = tadasets.swiss_roll(n=1000, r=10)
tadasets.plot3d(data)
```

## Contributions

This package is in the very early stages of development. As I think of shapes and data sets, I add them.  If you have ideas, please do suggest them in an issue and submit a pull request! All contributions are welcome.
