import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 100)
U, V = np.meshgrid(u, v)
X = (1 + 0.5*V*np.cos(U/2))*np.cos(U)
Y = (1 + 0.5*V*np.cos(U/2))*np.sin(U)
Z = 0.5*V*np.sin(U/2)

ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color='c', edgecolors='k')

plt.show()

