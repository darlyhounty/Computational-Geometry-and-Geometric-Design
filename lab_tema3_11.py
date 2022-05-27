import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from scipy.spatial import Delaunay
import datetime

data = np.random.rand(502, 2)

plt.subplots()
plt.axis('off')
plt.scatter(data[:,0],data[:,1])

plt.subplots()
tri=Delaunay(data)
plt.triplot(data[:,0], data[:,1], tri.simplices)
plt.plot(data[:,0], data[:,1], 'o')
plt.axis('off')
plt.show()

#
# #三角表格
# triangles = tri.Triangulation(data[:, 0], data[:, 1])
#
# plt.subplots()
# plt.axis('off')
# plt.scatter(data[:,0],data[:,1])
#
#
# plt.subplots()
# plt.axis('off')
# plt.triplot(triangles)
# plt.show()
