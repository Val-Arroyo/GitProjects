import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

hist_1 = np.random.randn(1000, 1);
hist_2 = np.random.randn(800, 1);

fig, axs = plt.subplots(1, 1, figsize = (8, 6), tight_layout = True);

axs.hist(hist_1, color = 'red', edgecolor = 'black', label = 
         );
axs.hist(hist_2, color = 'blue', edgecolor = 'black');

plt.grid();
plt.legend()
plt.xlabel();
plt.ylabel()
plt.show();