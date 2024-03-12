|PyPI version| |Downloads| |Codecov| |License: MIT|

This package provides some nice utilities for creating and loading data sets that are useful for Topological Data Analysis. Currently, we provide various synthetic data sets with particular topological features.


Setup
------

Installation is as easy as

.. code:: python

    pip install tadasets


Usage
------

The shape constructors are exposed in a functional interface, each returning a numpy array containing data sampled on the object. Available objects include

- torus
- d-sphere
- sphere
- swiss roll
- infinity sign
- eyeglasses

Each shape can be embedded in arbitrary ambient dimension by supplying the :code:`ambient` argument. Additionally, noise can be added to the shape through the :code:`noise` argument.

.. code:: python

    import tadasets

    torus = tadasets.torus(n=2000, c=2, a=1, ambient=200, noise=0.2)
    swiss_roll = tadasets.swiss_roll(n=2000, r=4, ambient=10, noise=1.2)
    dsphere = tadasets.dsphere(n=1000, d=12, r=3.14, ambient=14, noise=0.14)
    sphere = tadasets.sphere(n=500,seed=42)
    infty_sign = tadasets.infty_sign(n=3000, noise=0.1)
    eyeglasses = tadasets.eyeglasses(n=670,r1=10.0,r2=5.0)

Contributions
------------------

We welcome contributions of all shapes and sizes. There are lots of opportunities for potential projects, so please get in touch if you would like to help out. Everything from an implementation of your favorite distance, notebooks, examples, and documentation are all equally valuable so please don’t feel you can’t contribute.

If you have ideas for new shapes or features, please do suggest them in an issue and submit a pull request! 

To contribute please fork the project make your changes and submit a pull request. We will do our best to work through any issues with you and get your code merged into the main branch.



.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: User Guide

    reference/index
    notebooks/Examples

.. |Downloads| image:: https://img.shields.io/pypi/dm/tadasets
   :target: https://pypi.python.org/tadasets/
.. |PyPI version| image:: https://badge.fury.io/py/tadasets.svg
   :target: https://badge.fury.io/py/tadasets
.. |Codecov| image:: https://codecov.io/gh/scikit-tda/tadasets/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/scikit-tda/tadasets
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
