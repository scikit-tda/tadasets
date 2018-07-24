# TaDAsets
Data sets apt for Topological Data Analysis. This project is a part of scikit-tda.

# Motivation

At SoCG 2018, there was discussion about the need for data sets for two main purposes
- Benchmarking new algorithms
- Demonstrating benefits of TDA

# Data generation

We provide constructors for some synthetic data sets that are popular in development and testing of TDA techniques.

* Torus
* Klein Bottle
* Swiss Roll



# Setup and Usage

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



```
import tadasets
data = tadasets.swiss_roll(n=1000, r=10)
tadasets.plot3d(data)
```


