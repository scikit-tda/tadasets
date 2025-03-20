from tadasets.rotate import rotate_2D
import numpy as np
import pytest


def test_rotate_2D():
    with pytest.raises(ValueError) as ve:
        rotate_2D(np.array([[1, 2, 3], [4, 5, 6]]), 0)
        assert ve is not None
