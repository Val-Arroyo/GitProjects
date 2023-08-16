import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

year = [1972, 1982, 1992, 2002, 2012];
australia = [100.6, 158.61, 305.54, 394.96, 724.79];
new_zealand = [10.5, 25.21, 58.65, 119.27, 274.87];

plt.plot(year, australia, color='red', label='Australia', marker="" );
plt.plot(year, new_zealand, color='blue', label='New Zealand', marker="");


plt.xlabel("Years");
plt.ylabel("Power of consumption in kWh");

plt.legend();
plt.show();