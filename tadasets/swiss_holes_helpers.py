import numpy as np

def in_a_hole(row, centers, radiuses):
    """Helper function.

    Parameters
    ============

    row: entry in matrix
        One datapoint row.
    centers: np.ndarray with shape (n_holes, d)
        All the center coordinates of a ball.
    radiuses: np.ndarray with shape (n_holes, )
        All the radiuses of all the holes.
    """
    return any(np.apply_along_axis(np.linalg.norm,1,row - centers) <= radiuses) is False

def eliminate_overlaps(centers, radiuses, prioritize_bigger_balls):
    """Eliminates larger overlapping circles.
    TBD: Could probably be sped up using the miniball algorithm.

    Parameters
    ============

    centers: np.ndarray with shape (n_holes, d)
        All the center coordinates of a ball.
    radiuses: np.ndarray with shape (n_holes, )
        All the radiuses of all the holes.
    """
    inds = radiuses.argsort()
    if prioritize_bigger_balls is True:
        inds = inds[::-1]
    centers = centers[inds]
    radiuses = radiuses[inds]
    remove = set()
    for i in range(centers.shape[0]-1):
        for j in range(i+1,centers.shape[0]):
            if np.linalg.norm(centers[i] - centers[j]) <= (radiuses[i] + radiuses[j]):
                remove.add(j)
    return centers[[i for i in range(centers.shape[0]) if i not in remove]], radiuses[[i for i in range(centers.shape[0]) if i not in remove]]

def generate_swiss_holes(n_holes, d):
    """ Generates Swiss Cheese Holes

    Parameters
    ============
    n_holes: int
        number of holes in return data set.
    d: int
        number of dimensions
    """
    # Sample radiuses from a log-uniform distribution
    # Log uniform to ensure sizes vary reasonably
    radiuses = np.exp(np.random.uniform(np.log(0.2),np.log(0.5),size=n_holes))
    centers = np.random.uniform(-1,1,size=(n_holes,d))
    return centers, radiuses
