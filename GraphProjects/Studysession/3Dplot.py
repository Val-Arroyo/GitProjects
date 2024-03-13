import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

plt.style.use("dark_backg");
# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
z = np.zeros_like(x)

dx = np.ones_like(x)
dy = np.ones_like(y)
dz = [1, 2, 3, 4, 5]  # Heights of the bars

# Create 3D bar graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x, y, z, dx, dy, dz, color='skyblue')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.title('3D Bar Graph Example')
plt.show()