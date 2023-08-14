import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

np.random.seed(42);

xs = np.random.random(100) * 10 + 20

ys = np.random.random(100)* 5 + 7

zs = np.random.random(100)* 15 + 50

fig = plt.figure();

ax = fig.add_subplot(111, projection='3d');

ax.scatter(xs,ys,zs);

ax.set_title("Atom Velocity Distribution");

ax.set_xlabel("Atomic Mass (dalton)");

ax.set_ylabel("Atomic Radius(PM)");

ax.set_zlabel("Atomic Velocity(x10⁶ m/s)");

plt.show();