import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib import style


# Data for the stacked bar graph
x = np.array([1, 2, 3, 4, 5])  # X coordinates
y = np.array([1, 2, 3, 4, 5])  # Y coordinates
z = np.zeros(len(x))  # Z coordinates (start at 0 for the first layer)
dx = np.ones(len(x))  # Width of each bar along the x-axis
dy = np.ones(len(y))  # Width of each bar along the y-axis
dz1 = np.array([1, 2, 3, 4, 5])  # Heights of the first stack
dz2 = np.array([2, 3, 4, 5, 6])  # Heights of the second stack

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first stack
ax.bar3d(x, y, z, dx, dy, dz1, color='b')

# Plot the second stack on top of the first stack
ax.bar3d(x, y, dz1, dx, dy, dz2, color='r')

# Customize labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('Stacked Bar Graph in 3D')

# Show the plot
plt.show()
