
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
data = np.random.rand(200, 2)

#三角表格
triangles = tri.Triangulation(data[:, 0], data[:, 1])

plt.subplots()
plt.axis('off')
plt.scatter(data[:,0],data[:,1])


plt.subplots()
plt.axis('off')
plt.triplot(triangles)
plt.show()
