"""
    I'm not sure the best way to test that the shapes are correct, 
    so visual testing will be easier 

"""

import matplotlib.pyplot as plt
import tadasets


t = tadasets.torus(n=345)
tadasets.plot3d(t)

plt.show()