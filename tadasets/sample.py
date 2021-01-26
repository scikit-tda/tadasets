"""
    Methods for constructing point clouds from meshes.

"""

import numpy as np


def from_mesh(vertices, triangles, n=1000):
    """
    Randomly sample points by area on a triangle mesh.  This function is
    extremely fast by using broadcasting/numpy operations in lieu of loops

    Inputs
    -------
    vertices : ndarray (N, 3)
        Array of points in 3D
    triangles : ndarray (M, 3)
        Array of triangles connecting points, pointing to vertex indices
    n : int
        Number of points to sample

    Returns
    -------
    data : NDArray (n, 3) array of sampled points

    """

    assert vertices.shape[1] == 3
    assert triangles.shape[1] == 3

    # Step 1: Compute cross product of all face triangles and use to compute
    # areas (very similar to code used to compute vertex normals)

    # Vectors spanning two triangle edges
    P0 = vertices[triangles[:, 0], :]
    P1 = vertices[triangles[:, 1], :]
    P2 = vertices[triangles[:, 2], :]
    V1 = P1 - P0
    V2 = P2 - P0
    FNormals = np.cross(V1, V2)
    # import pdb; pdb.set_trace()
    FAreas = np.sqrt(np.sum(FNormals ** 2, 1)).flatten()

    # Get rid of zero area faces and update points
    triangles = triangles[FAreas > 0, :]
    FNormals = FNormals[FAreas > 0, :]
    FAreas = FAreas[FAreas > 0]
    P0 = vertices[triangles[:, 0], :]
    P1 = vertices[triangles[:, 1], :]
    P2 = vertices[triangles[:, 2], :]

    # Compute normals
    NTris = triangles.shape[0]
    FNormals = FNormals / FAreas[:, None]
    FAreas = 0.5 * FAreas
    FNormals = FNormals
    # VNormals = np.zeros_like(vertices)
    VAreas = np.zeros(vertices.shape[0])
    for k in range(3):
        # VNormals[triangles[:, k], :] += FAreas[:, None] * FNormals
        VAreas[triangles[:, k]] += FAreas

    # Normalize normals
    VAreas[VAreas == 0] = 1
    # VNormals = VNormals / VAreas[:, None]

    # Step 2: Randomly sample points based on areas
    FAreas = FAreas / np.sum(FAreas)
    AreasC = np.cumsum(FAreas)
    samples = np.sort(np.random.rand(n))

    # Figure out how many samples there are for each face
    FSamples = np.zeros(NTris, np.int64)
    fidx = 0
    for s in samples:
        while s > AreasC[fidx]:
            fidx += 1
        FSamples[fidx] += 1

    # Now initialize an array that stores the triangle sample indices
    tidx = np.zeros(n, dtype=np.int64)
    idx = 0
    for i in range(len(FSamples)):
        tidx[idx : idx + FSamples[i]] = i
        idx += FSamples[i]
    # N = np.zeros((n, 3))  # Allocate space for normals
    idx = 0

    # Vector used to determine if points need to be flipped across parallelogram
    V3 = P2 - P1
    V3 = V3 / np.sqrt(np.sum(V3 ** 2, 1))[:, None]  # Normalize

    # Randomly sample points on each face
    # Generate random points uniformly in parallelogram
    u = np.random.rand(n, 1)
    v = np.random.rand(n, 1)
    Ps = u * V1[tidx, :] + P0[tidx, :]
    Ps += v * V2[tidx, :]

    # Flip over points which are on the other side of the triangle
    dP = Ps - P1[tidx, :]
    proj = np.sum(dP * V3[tidx, :], 1)
    dPPar = V3[tidx, :] * proj[:, None]  # Parallel project onto edge
    dPPerp = dP - dPPar
    Qs = Ps - dPPerp
    dP0QSqr = np.sum((Qs - P0[tidx, :]) ** 2, 1)
    dP0PSqr = np.sum((Ps - P0[tidx, :]) ** 2, 1)
    idxreg = np.arange(n, dtype=np.int64)
    idxflip = idxreg[dP0QSqr < dP0PSqr]
    u[idxflip, :] = 1 - u[idxflip, :]
    v[idxflip, :] = 1 - v[idxflip, :]
    Ps[idxflip, :] = (
        P0[tidx[idxflip], :]
        + u[idxflip, :] * V1[tidx[idxflip], :]
        + v[idxflip, :] * V2[tidx[idxflip], :]
    )

    # # Step 3: Compute normals of sampled points by barycentric interpolation
    # Ns = u * VNormals[triangles[tidx, 1], :]
    # Ns += v * VNormals[triangles[tidx, 2], :]
    # Ns += (1 - u - v) * VNormals[triangles[tidx, 0], :]

    return Ps


__all__ = ["from_mesh"]
