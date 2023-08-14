import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

#data generation for 1st plot
np.random.seed(42)

xs = np.random.random(100)  * 10 + 20

ys = np.random.random(100) * 5 + 7

zs = np.random.random(100) * 15 + 50

#data generation for 2nd plot
np.random.seed(42)

ages = np.random.randint(low = 8, high = 30, size=35)

heights = np.random.randint(130, 195, 35)

weights = np.random.randint(30, 160, 35)

fig = plt.figure(figsize = (8,4))

#First plot
ax = fig.add_subplot(121, projection='3d')

ax.scatter(xs,ys,zs, marker="x", c="red")

ax.set_title("Atom velocity distribution")

ax.set_xlabel("Atomic mass (dalton)")

ax.set_ylabel("Atomic radius (pm)")

ax.set_zlabel("Atomic velocity (x10⁶ m/s)")

#Second plot
ax = fig.add_subplot(122, projection='3d')

ax.scatter(xs = heights, ys = weights, zs = ages)

ax.set_title("Age-wise body weight-height distribution")

ax.set_xlabel("Height (cm)")

ax.set_ylabel("Weight (kg)")

ax.set_zlabel("Age (years)")

plt.show() 

