import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
import pandas 
from matplotlib.ticker import PercentFormatter
from matplotlib import colors
from numpy.lib.histograms import histogram

graph1 = np.random.randn(500, 1);
graph2 = np.random.randn(400, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.hist(graph1, color = 'red', alpha = 0.8, edgecolor = 'black');
axs.hist(graph2, color = 'blue', alpha = 0.7, edgecolor = 'white');

axs.grid(color = 'red', linewidth = 0.7, linestyle = '-.');
plt.show();