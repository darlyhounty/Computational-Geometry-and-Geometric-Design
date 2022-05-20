

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import pcolormesh
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)

X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)

plt.figure()
ax1 = plt.axes(projection='3d')
ax1.plot_surface(X,Y,Z,alpha=1,cmap='winter')

ax1.contourf(X,Y,Z,zdir='z', offset=0,cmap="rainbow")

fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp)
plt.show()
