import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

z = np.random.randint(100, size=(50));
x = np.random.randint(80, size = (50));
y = np.random.randint(60, size = (50));

fig = plt.figure();

ax = plt.axes(projection = "3d");

plt.show();