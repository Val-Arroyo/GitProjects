import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d



plt.style.use("dark_background")

fig = plt.figure(figsize = (10, 7));
ax = plt.axes(projection = "3d");

ax.hist3D(x, y, z, color = "white")
plt.title("Simple 3D Scatter Plot")

plt.show();