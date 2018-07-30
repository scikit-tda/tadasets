import numpy as np
import matplotlib
matplotlib.use('Agg')

import tadasets
from scipy.spatial.distance import pdist

def norm(p):
    return np.sum(p**2)**0.5

class TestEmbedding:
    def test_shape(self):
        d = np.random.random((100, 3))
        d_emb = tadasets.embed(d, 10)
        assert d_emb.shape == (100, 10)
    
    def test_rotated(self):
        """ No variables should be all zero.
        Nonzero variance implies some transformation happened.
        """
        d = np.random.random((100, 3))
        d_emb = tadasets.embed(d, 10)
        assert np.all(np.var(d_emb, axis=0) > 0)

    def test_dist_matrix_same(self):
        d = np.random.random((100, 3))
        dists = pdist(d)

        d_emb = tadasets.embed(d, 10)
        dists_emb = pdist(d_emb)

        np.testing.assert_almost_equal(dists_emb, dists)


class TestSphere:
    def test_n(self):
        s = tadasets.sphere(n=543)
        assert s.shape[0] == 543
    
    def test_r(self):
        r = 23
        bf = 1e-5
        s = tadasets.sphere(r=r)
        rs = np.fromiter((norm(p) for p in s), np.float64)
        print(np.all(rs <= r+bf))

    def test_ambient(self):
        s = tadasets.sphere(n=200, r=3, ambient=15)
        assert s.shape == (200, 15)


class TestTorus:
    def test_n(self):
        t = tadasets.torus(n=345)
        assert t.shape[0] == 345
    
    def test_bounds(self):
        c, a = 3, 2
        t = tadasets.torus(n=3045, c=3, a=2)

        bound = c + a
        rs = np.fromiter((norm(p) for p in t), np.float64)
        assert np.all(rs <= bound)

    def test_plt(self):
        t = tadasets.torus(n=345)
        tadasets.plot3d(t)
    
    def test_ambient(self):
        s = tadasets.torus(n=200, c=3, ambient=15)
        assert s.shape == (200, 15)


class TestSwissRoll:
    def test_n(self):
        t = tadasets.swiss_roll(n=345)
        assert t.shape[0] == 345

    def test_plt(self):
        t = tadasets.swiss_roll(n=345)
        tadasets.plot3d(t)
            
    def test_ambient(self):
        s = tadasets.swiss_roll(n=200, ambient=15)
        assert s.shape == (200, 15)

