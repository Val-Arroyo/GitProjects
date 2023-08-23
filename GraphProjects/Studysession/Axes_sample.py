import matplotlib.pyplot as plt
import numpy as np

x = [2000, 2005, 2010, 2015, 2020];

fig, ax = plt.subplot();

ax.pie(x);

plt.show();