import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d

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

# Generate data for the scatter plot
np.random.seed(0)
x_scatter = np.random.standard_normal(100)
y_scatter = np.random.standard_normal(100)
z_scatter = np.random.standard_normal(100)

# Generate data for the bar graph
x_bar = np.array([1, 2, 3, 4, 5])
y_bar = np.array([1, 2, 3, 4, 5])
z_bar = np.zeros(len(x_bar))
dx_bar = np.ones(len(x_bar))
dy_bar = np.ones(len(y_bar))
dz_bar = np.array([1, 2, 3, 4, 5])

# Create a figure and four subplots
fig = plt.figure(figsize=(12, 12))

# First subplot for the surface plot
ax_surf = fig.add_subplot(221, projection='3d')
surf = ax_surf.plot_surface(x_surf, y_surf, z_surf, cmap='viridis')
ax_surf.set_title('Surface Plot')

# Second subplot for the wireframe plot
ax_wire = fig.add_subplot(222, projection='3d')
wire = ax_wire.plot_wireframe(x_wire, y_wire, z_wire, color='r')
ax_wire.set_title('Wireframe Plot')

# Third subplot for the scatter plot
ax_scatter = fig.add_subplot(223, projection='3d')
scatter = ax_scatter.scatter(x_scatter, y_scatter, z_scatter, c='g', marker='o')
ax_scatter.set_title('Scatter Plot')

# Fourth subplot for the bar graph
ax_bar = fig.add_subplot(224, projection='3d')
bar = ax_bar.bar3d(x_bar, y_bar, z_bar, 1, 1, dz_bar, color='b')
ax_bar.set_title('Bar Graph')

# Show the plots
plt.tight_layout()
plt.show()