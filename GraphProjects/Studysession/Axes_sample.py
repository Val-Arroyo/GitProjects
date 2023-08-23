import matplotlib.pyplot as plt
import numpy as np

x = [2000, 2005, 2010, 2015, 2020];
y = [10000, 20000, 30000, 40000, 50000];
z = [1000000, 2000000, 3000000, 4000000, 5000000]

fig, ax = plt.subplots(2);

ax[1].plot(x, y);


plt.show();