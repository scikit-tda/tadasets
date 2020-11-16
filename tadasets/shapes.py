import numpy as np
from .dimension import embed
from .rotate import rotate_2D
from .custom_exceptions import RotationAngleNotInRangeError
from .swiss_holes_helpers import in_a_hole, eliminate_overlaps, generate_swiss_holes
__all__ = ["torus", "dsphere", "sphere", "swiss_roll", "infty_sign", "d_swiss_cheese"]


## TODO: Make a base class that controls `ambient` and `noise`.
class Shape:
    def __init__(self):
        pass


def dsphere(n=100, d=2, r=1, noise=None, ambient=None):
    """
    Sample `n` data points on a d-sphere.

    Parameters
    -----------
    n : int
        Number of data points in shape.
    r : float
        Radius of sphere.
    ambient : int, default=None
        Embed the sphere into a space with ambient dimension equal to `ambient`. The sphere is randomly rotated in this high dimensional space.
    """
    data = np.random.randn(n, d+1)

    # Normalize points to the sphere
    data = r * data / np.sqrt(np.sum(data**2, 1)[:, None])

    if noise:
        data += noise * np.random.randn(*data.shape)

    if ambient:
        assert ambient > d, "Must embed in higher dimensions"
        data = embed(data, ambient)



    return data


def sphere(n=100, r=1, noise=None, ambient=None):
    """
        Sample `n` data points on a sphere.

    Parameters
    -----------
    n : int
        Number of data points in shape.
    r : float
        Radius of sphere.
    ambient : int, default=None
        Embed the sphere into a space with ambient dimension equal to `ambient`. The sphere is randomly rotated in this high dimensional space.
    """

    theta = np.random.random((n,)) * 2.0 * np.pi
    phi = np.random.random((n,)) * np.pi
    rad = np.ones((n,)) * r

    data = np.zeros((n, 3))

    data[:, 0] = rad * np.cos(theta) * np.cos(phi)
    data[:, 1] = rad * np.cos(theta) * np.sin(phi)
    data[:, 2] = rad * np.sin(theta)


    if noise:
        data += noise * np.random.randn(*data.shape)

    if ambient:
        data = embed(data, ambient)

    return data


def torus(n=100, c=2, a=1, noise=None, ambient=None):
    """
    Sample `n` data points on a torus.

    Parameters
    -----------
    n : int
        Number of data points in shape.
    c : float
        Distance from center to center of tube.
    a : float
        Radius of tube.
    ambient : int, default=None
        Embed the torus into a space with ambient dimension equal to `ambient`. The torus is randomly rotated in this high dimensional space.
    """

    assert a <= c, "That's not a torus"

    theta = np.random.random((n,)) * 2.0 * np.pi
    phi = np.random.random((n,)) * 2.0 * np.pi

    data = np.zeros((n, 3))
    data[:, 0] = (c + a * np.cos(theta)) * np.cos(phi)
    data[:, 1] = (c + a * np.cos(theta)) * np.sin(phi)
    data[:, 2] = a * np.sin(theta)

    if noise:
        data += noise * np.random.randn(*data.shape)

    if ambient:
        data = embed(data, ambient)

    return data


def swiss_roll(n=100, r=10, noise=None, ambient=None):
    """Swiss roll implementation

    Parameters
    ----------
    n : int
        Number of data points in shape.
    r : float
        Length of roll
    ambient : int, default=None
        Embed the swiss roll into a space with ambient dimension equal to `ambient`. The swiss roll is randomly rotated in this high dimensional space.

    References
    ----------
    Equations mimic [Swiss Roll and SNE by jlmelville](https://jlmelville.github.io/smallvis/swisssne.html)
    """

    phi = (np.random.random((n,)) * 3 + 1.5) * np.pi
    psi = np.random.random((n,)) * r

    data = np.zeros((n, 3))
    data[:, 0] = phi * np.cos(phi)
    data[:, 1] = phi * np.sin(phi)
    data[:, 2] = psi

    if noise:
        data += noise * np.random.randn(*data.shape)

    if ambient:
        data = embed(data, ambient)

    return data

def infty_sign(n=100, noise=None, angle=None):
    """Construct a figure 8 or infinity sign with :code:`n` points and noise level with :code:`noise` standard deviation.

    Parameters
    ============

    n: int
        number of points in returned data set.
    noise: float
        standard deviation of normally distributed noise added to data.
    angle: float
        angle in radians to rotate the infinity sign.
    """


    t = np.linspace(0, 2*np.pi, n+1)[0:n]
    X = np.zeros((n, 2))
    X[:, 0] = np.cos(t)
    X[:, 1] = np.sin(2*t)

    if noise:
        X += noise * np.random.randn(n, 2)

    if angle is not None:
        try:
            assert angle >= -np.pi and angle <= 2*np.pi
        except AssertionError:
            raise RotationAngleNotInRangeError(angle, 0, "pi")

        X = rotate_2D(X, angle=angle)

    return X

def d_swiss_cheese(n_points=10000, n_holes=4, d=2, noise=None, seed=None, non_overlapping=False, prioritize_bigger_balls=False):
    """ Creates a square-formed swiss cheese manifold in d dimensions.

    Parameters
    ============

    n_points: int
        number of points in returned data set.
    n_holes: int
        number of holes in return data set.
    d: int
        number of dimensions
    """
    if seed is not None:
        np.random.seed(seed)

    points = np.random.uniform(-1,1, size=(n_points, d))
    centers, radiuses = generate_swiss_holes(n_holes, d)
    if non_overlapping is True:
        # Disregard overlaps
        centers, radiuses = eliminate_overlaps(centers, radiuses, prioritize_bigger_balls=prioritize_bigger_balls)
        while centers.shape[0] < n_holes:
            c, r = generate_swiss_holes(n_holes - centers.shape[0], d)
            centers, radiuses = eliminate_overlaps(np.concatenate([centers,c],axis=0),np.concatenate([radiuses, r],axis=0), prioritize_bigger_balls=prioritize_bigger_balls)
    points = points[np.apply_along_axis(in_a_hole,1,points,centers,radiuses),:]
    while points.shape[0] < n_points:
        ps = np.random.uniform(-1,1, size=((n_points-points.shape[0]), d))
        ps = ps[np.apply_along_axis(in_a_hole,1,ps,centers,radiuses),:]
        points = np.concatenate([points,ps],axis=0)

    if noise:
        points += noise * np.random.randn(*data.shape)
    return points
