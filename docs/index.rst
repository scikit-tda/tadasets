.. tadasets documentation master file, created by
   sphinx-quickstart on Sun Jul 22 20:37:23 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


|PyPI version| |Travis-CI| |Appveyor| |Codecov| |License: LGPL v3|

Ripser
========

This package provides some nice utilities for creating and loading data sets that are useful for Topological Data Analysis. Currently, we provide various synthetic data sets with particular topological features.


Setup
------

Installation requires Cython, and currently must be installed from source. An example of how to install is

.. code:: python

    pip install tadasets


Usage
------

.. code:: python

    import tadasets

    torus = tadasets.torus(n=2000)


.. toctree::
    :maxdepth: 2
    :caption: Usage:

    Show shapes
    reference

 
.. |PyPI version| image:: https://badge.fury.io/py/tadasets.svg
   :target: https://badge.fury.io/py/tadasets

.. |Travis-CI| image:: https://travis-ci.org/scikit-tda/tadasets.svg?branch=master
    :target: https://travis-ci.org/scikit-tda/tadasets

.. |Codecov| image:: https://codecov.io/gh/ctralie/ripser/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ctralie/ripser
.. |License: LGPL v3| image:: https://img.shields.io/badge/License-LGPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0
