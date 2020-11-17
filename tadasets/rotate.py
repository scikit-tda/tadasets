import numpy as np


def get_phi(row):
    """Helper function for rotating data.

    row: 2D-entry in matrix with shape (?, 2)
    """
    return np.arctan2(row[0], row[1])


def rotate_2D(d, angle):
    """Rotate a 2-dimensional figure.

    Parameters
    ============

    d: the 2-dimensional data to rotate
    angle: the angle (in radians) to rotate the data around 0
    centered_around_zero: Boolean specifying whether the data is centered around zero.
    """
    try:
        assert d.shape[1] == 2
    except AssertionError:
        raise ValueError(
            "Error: data has {} dimensions, but should only be 2. ".format(d.shape[1])
        )

    rot = angle - np.pi / 2
    phis = np.apply_along_axis(get_phi, 1, d)
    phi_new = phis + rot
    r = np.sqrt(d[:, 0] ** 2 + d[:, 1] ** 2)

    x = r * np.cos(phi_new)
    y = r * np.sin(phi_new)
    return np.concatenate((x.reshape(-1, 1), y.reshape(-1, 1)), axis=1)
