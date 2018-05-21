import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)

x = np.arange(-5, 5, .25)
y = np.arange(-5, 5, .25)
x, y = np.meshgrid(x, y)
z = np.sin(x) * np.cos(y) // np.tan(x/y)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=pl.cm.hot)
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(-2, 2)
pl.show()
