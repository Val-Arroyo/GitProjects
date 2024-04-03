import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some random data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.sin(x * y * np.pi)  # Some arbitrary function

# Create a triangulation from the data
tri = Triangulation(x, y)

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the triangular surface
ax.plot_trisurf(tri, z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Triangular Surface Plot')

# Show the plot
plt.show()
