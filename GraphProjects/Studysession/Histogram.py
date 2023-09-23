import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

hist_1 = np.random.randn(500, 1);
hist_2 = np.random.randn(400, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.hist(hist_1, edgecolor = 'black', label = 'First Histogram');
axs.hist(hist_2, edgecolor = 'black', label = 'Second Histogram');

axs.xaxis.set_tick_params(pad = 5)
axs.yaxis.set_tick_params(pad = 10);

plt.grid(color = 'black', linestyle = '-.', linewidth = 0.5);
plt.legend()
plt.xlabel("X Label");
plt.ylabel("Y Label")
plt.show();