import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot3d(data):
    fig = plt.figure()
       
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0], data[:,1], data[:,2])
