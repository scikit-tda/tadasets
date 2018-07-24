import numpy as np


def sphere(n=100, r=1):
    """
        Sample `n` data points on a sphere.

    Parameters
    -----------
    n : int
        Number of data points in shape.
    r : float
        Radius of sphere.
    """

    theta = np.random.random((n, )) * 2.0 * np.pi
    phi = np.random.random((n, )) * np.pi
    rad = np.ones((n, )) * r

    data = np.zeros((n, 3))

    data[:, 0] = rad * np.cos(theta) * np.cos(phi)
    data[:, 1] = rad * np.cos(theta) * np.sin(phi)
    data[:, 2] = rad * np.sin(theta)   

    return data

def torus(n=100, c=2, a=1):
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
    """
    
    assert a <= c, "That's not a torus"

    theta = np.random.random((n,)) * 2.0 * np.pi
    phi = np.random.random((n,)) * 2.0 * np.pi

    data = np.zeros((n, 3))
    data[:,0] = (c + a * np.cos(theta)) * np.cos(phi)
    data[:,1] = (c + a * np.cos(theta)) * np.sin(phi)
    data[:,2] = a * np.sin(theta)
    
    return data

def swiss_roll(n=100, r=10):
    """Swiss roll implementation

    Parameters
    ----------
    n : int 
        Number of data points in shape.
    r : float
        Length of roll

    References
    ----------
    Equations mimic [Swiss Roll and SNE by jlmelville](https://jlmelville.github.io/smallvis/swisssne.html)
    """

    phi = (np.random.random((n, )) * 3 + 1.5) * np.pi
    psi = np.random.random((n, )) * r

    data = np.zeros((n, 3))
    data[:, 0] = phi * np.cos(phi)
    data[:, 1] = phi * np.sin(phi)
    data[:, 2] = psi

    return data


__all__ = ["torus", "sphere", "swiss_roll"]