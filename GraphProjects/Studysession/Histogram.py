import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.ticker as mtick
from matplotlib import colors
from numpy.lib.histograms import histogram
from matplotlib.ticker import PercentFormatter

Hist_1 = np.random.randn(500, 1);
Hist_2 = np.random.randn(300, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.hist(Hist_1, color = 'red', edgecolor = 'black');
axs.hist(Hist_2, color = 'blue');