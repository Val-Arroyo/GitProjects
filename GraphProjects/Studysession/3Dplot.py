import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

data = np.random.randn(1000)

plt.style.use("dark_background")

fig = plt.figure(figsize = (10, 7));
ax = plt.axes(projection = "3d");

ax.hist3D(data, bins = 30, color = "skyblue", edgecolor = "")
plt.title("Simple 3D Scatter Plot")

plt.show();