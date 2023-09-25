import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

Hist_1 = np.random.randn(300, 1);
Hist_2 = np.random.randn(200, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.hist(Hist_1, color = 'red', edgecolor = 'black', );
axs.hist(Hist_2, color = 'blue', edgecolor = 'black');

plt.grid(color = 'red', linestyle = '-.', );
plt.legend();
plt.xlabel();
plt.ylabel();

plt.show();