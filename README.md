# TaDAsets
Data sets apt for Topological Data Analysis. A part of scikit-tda.

At SoCG 2018, there was discussion about the need for data sets for two main purposes
- Benchmarking new algorithms
- Demonstrating benefits of TDA


# Data generation

Build a generator to construct arbitrary genus data sets. It should take a list of integers with the $i$th index representing $\beta_i$. This should construct a manifold with the proper betti numbers, which can then be sampled with the desired quantity and noise levels.

How hard of a problem is this?

```
class HomGen:
  def __init__(self, betti: list, n: int, noise: float):
    pass
```

# Example Sets

What data sets are good for tda? IDK!
