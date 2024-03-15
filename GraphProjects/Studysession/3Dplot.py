import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits

# Data for the bar graph
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = np.zeros((len(x), len(y)))
dx = np.ones((len(x), len(y)))
dy = np.ones((len(x), len(y)))
dz = [1, 2, 3, 4, 5]  # Heights of the bars

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D bars
ax.bar3d(x, y, z, dx, dy, dz)

# Customize labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('3D Bar Graph')

# Show the plot
plt.show()