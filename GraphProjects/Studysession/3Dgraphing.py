import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Data
x = np.arange(1, 6)  # X coordinates of bars
y = np.zeros(5)       # Y coordinates of bars (all zero for the base)
z = np.arange(1, 6)   # Z coordinates of bars (heights)

# Heights for each stacked section (three sets of stacked bars)
dz1 = np.array([1, 2, 3, 4, 5])
dz2 = np.array([2, 3, 4, 5, 6])
dz3 = np.array([3, 4, 5, 6, 7])

# Colors for each stacked section
colors1 = ['r', 'g', 'b', 'y', 'c']
colors2 = ['c', 'm', 'y', 'k', 'b']
colors3 = ['b', 'g', 'r', 'c', 'm']

# Plot bars
for i in range(len(x)):
    ax.bar3d(x[i], y, z, 0.5, 0.5, dz1[i], color=colors1[i])
    ax.bar3d(x[i], y, z, 0.5, 0.5, dz2[i], color=colors2[i])
    ax.bar3d(x[i], y, z, 0.5, 0.5, dz3[i], color=colors3[i])

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Multiple Stacked 3D Bar Graph')

plt.show()



