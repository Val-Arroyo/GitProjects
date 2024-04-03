import matplotlib.pyplot 

# Define the function to plot
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a figure and a 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add contour projections in the xy plane
ax.contour(X, Y, Z, zdir='z', offset=-2, cmap='viridis')

# Add contour projections in the xz plane
ax.contour(X, Y, Z, zdir='y', offset=-5, cmap='viridis')

# Add contour projections in the yz plane
ax.contour(X, Y, Z, zdir='x', offset=-5, cmap='viridis')

# Add a color bar which maps values to colors
fig.colorbar(surf)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot with Contour Projections')

# Show the plot
plt.show()
