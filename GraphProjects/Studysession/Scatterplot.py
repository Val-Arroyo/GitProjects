import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors


x_value = np.array([1, 2, 3, 4, 5, 6]);

y_value = np.array([10, 30, 50, 70, 90, 110]);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.scatter(x_value, y_value, color = 'red', marker = '^', edgecolors = 'black', size = 0.5);

plt.show();