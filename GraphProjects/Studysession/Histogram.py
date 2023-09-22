import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from numpy.lib.histograms 

graph_1 = np.random.randn(1000, 1);
graph_2 = np.random.randn(500, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.hist(graph_1, color = 'red', edgecolor = 'black', label = 'First Histogram');
axs.hist(graph_2, color = 'blue', edgecolor = 'black', label = 'Second Histogram');

plt.grid(color = 'red', linestyle = '-.', linewidth = 0.6);
plt.legend()
plt.show();

