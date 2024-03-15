import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for the surface plot
x_surf = np.linspace(-5, 5, 100)
y_surf = np.linspace(-5, 5, 100)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z_surf = np.sin(np.sqrt(x_surf**2 + y_surf**2))

# Generate data for the wireframe plot
x_wire = np.linspace(-5, 5, 10)
y_wire = np.linspace(-5, 5, 10)
x_wire, y_wire = np.meshgrid(x_wire, y_wire)
z_wire = np.sin(np.sqrt(x_wire**2 + y_wire**2))

# Create a figure and two subplots
fig = plt.figure(figsize=(12, 6))

# First subplot for the surface plot
ax_surf = fig.add_subplot(121, projection='3d')
surf = ax_surf.plot_surface(x_surf, y_surf, z_surf, cmap='viridis')
ax_surf.set_title('Surface Plot')

# Second subplot for the wireframe plot
ax_wire = fig.add_subplot(122, projection='3d')
wire = ax_wire.plot_wireframe(x_wire, y_wire, z_wire, color='r')
ax_wire.set_title('Wireframe Plot')

# Show the plots
plt.show()
