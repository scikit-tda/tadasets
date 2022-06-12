import numpy as np
import pytest
import tadasets
from scipy.spatial.distance import pdist


def norm(p):
    return np.sum(p ** 2) ** 0.5


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
        s = tadasets.sphere(r=r)
        rs = np.fromiter((norm(p) for p in s), np.float64)
        assert np.all(rs <= r + 1e-5)
        assert np.all([r - 1e-5 <= rx <= r + 1e-5 for rx in rs])

    def test_ambient(self):
        s = tadasets.sphere(n=200, r=3, ambient=15)
        assert s.shape == (200, 15)


class TestDsphere:
    def test_d(self):
        s = tadasets.dsphere(n=100, d=2)
        assert s.shape[1] == 3

    def test_equivalence(self):
        s = tadasets.dsphere(n=100, d=2)
        rs = np.fromiter((norm(p) for p in s), np.float64)
        assert np.all([1 - 1e-5 <= r <= 1 + 1e-5 for r in rs])

    def test_r(self):
        s = tadasets.dsphere(n=100, d=2, r=4)
        rs = np.fromiter((norm(p) for p in s), np.float64)
        assert np.all([4 - 1e-5 <= r <= 4 + 1e-5 for r in rs])


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


class TestInfty:
    def test_n(self):
        t = tadasets.infty_sign(n=345)
        assert t.shape[0] == 345

    def test_rotation(self):
        with pytest.raises(AssertionError) as ae:
            t = tadasets.infty_sign(n=345, angle=-100)
            assert ae is not None
        with pytest.raises(AssertionError) as ae:
            t = tadasets.infty_sign(n=345, angle=300)
            assert ae is not None
        t = tadasets.infty_sign(n=345, angle=2)
        assert t.shape[0] == 345


class TestEyeglasses:
    def test_n(self):
        t = tadasets.eyeglasses(n=345, r1=1, r2=2, neck_size=.8)
        assert t.shape[0] == 345

    def test_neck(self):
        t = tadasets.eyeglasses(n=5000, r1=1, r2=2, neck_size=.8)
        top, bottom = t[t[:, 1] > 0], t[t[:, 1] < 0]
        y_neck_top = top[np.abs(top[:, 0]).argmin(), 1]
        y_neck_bottom = bottom[np.abs(bottom[:, 0]).argmin(), 1]
        assert np.abs(y_neck_top - y_neck_bottom - .8) <= .001

    def test_r(self):
        t = tadasets.eyeglasses(n=5000, r1=1, r2=2, neck_size=.8)
        left, right = t[t[:, 0] < 0], t[t[:, 0] > 0]
        assert np.abs(left[:, 1].max() - 1) <= .001
        assert np.abs(right[:, 1].max() - 2) <= .001
