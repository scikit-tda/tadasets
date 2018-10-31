"""
    Methods for embedding objects in high dimensional space.

"""

import numpy as np


def embed(data, ambient=50):
    """ Embed `data` in `ambient` dimensions, regardless of dimensionality of data.

    Inputs
    ------
    data : array-like

    ambient : int
        Dimension of embedding space. Must be greater than dimensionality of data.
    """

    n, d = data.shape
    assert (
        ambient > d
    ), "Dimensionality of ambient space ({}) must be greater than dimensionality of data ({}).".format(
        ambient, d
    )

    base = np.zeros((n, ambient))
    base[:, :d] = data

    # construct a rotation matrix of dimension `ambient`.
    random_rotation = np.random.random((ambient, ambient))
    q, r = np.linalg.qr(random_rotation)

    base = np.dot(base, q)

    return base


__all__ = ["embed"]
