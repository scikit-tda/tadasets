import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot3d(data, fig=None, ax=None):
    fig = fig if fig else plt.figure()

    ax = ax if ax else fig.add_subplot(111, projection="3d")
    ax.scatter(data[:, 0], data[:, 1], data[:, 2])
    return ax
