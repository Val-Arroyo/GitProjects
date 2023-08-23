import matplotlib.pyplot as plt
import numpy as np

x = [2000, 2005, 2010, 2015, 2020];
y = [10000, 20000, 30000, 40000, 50000];

fig, ax = plt.subplot(1, 3);

ax.plot(x, y);

plt.show();