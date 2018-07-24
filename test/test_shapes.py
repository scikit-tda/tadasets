import numpy as np

import tadasets


def norm(p):
    return np.sum(p**2)**0.5


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


class TestSwissRoll:
    def test_n(self):
        t = tadasets.swiss_roll(n=345)
        assert t.shape[0] == 345

    def test_plt(self):
        t = tadasets.swiss_roll(n=345)
        tadasets.plot3d(t)