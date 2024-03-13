import matplotlib.pyplot as 

z = np.random.randint(100, size = (50));
x = np.random.randint(80, size = (50));
y = np.random.randint(60, size = (50));

plt.style.use("dark_background")

fig = plt.figure(figsize = (10, 7));
ax = plt.axes(projection = "3d");

ax.scatter3D(x, y, z, color = "white")
plt.title("Simple 3D Scatter Plot")

plt.show();