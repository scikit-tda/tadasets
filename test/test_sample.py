import numpy as np


from tadasets.sample import from_mesh


class TestMeshSampler:
    def test_unit_square(self):

        vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])

        tris = np.array([[0, 1, 2], [1, 2, 3]])

        points = from_mesh(vertices, tris, n=100)

        assert np.max(points) <= 1
        assert np.min(points) >= 0

    def test_n(self):
        vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])

        tris = np.array([[0, 1, 2], [1, 2, 3]])

        points = from_mesh(vertices, tris, n=100)

        assert len(points) == 100

    def test_single_triangle(self):
        vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])

        tris = np.array([[0, 1, 2]])

        points = from_mesh(vertices, tris, n=100)

        assert np.all(points[:, 0] + points[:, 1] <= 1)
        assert len(points) == 100
