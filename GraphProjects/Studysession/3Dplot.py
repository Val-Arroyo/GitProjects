import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
x, y = np.meshgrid(np.arange(10), np.arange(10))
z = np.random.rand(10, 10) * 10
colors = np.random.rand(10, 10, 3)  # Random colors for each bar

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create 3D bars
ax.bar3d(x.flatten(), y.flatten(), np.zeros_like(z.flatten()), 1, 1, z.flatten(), color=colors, zsort='average')

# Customize ticks and labels
ax.set_xticks(np.arange(10) + 0.5)
ax.set_yticks(np.arange(10) + 0.5)
ax.set_xticklabels(np.arange(10))
ax.set_yticklabels(np.arange(10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add annotations
for xi in range(10):
    for yi in range(10):
        ax.text(xi + 0.5, yi + 0.5, z[xi, yi], '%.2f' % z[xi, yi], color='black', ha='center', va='center')

# Title and show
plt.title('3D Bar Graph')
plt.show()