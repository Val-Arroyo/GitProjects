import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

random_number_generator = np.random.normal(240, 15, 250);
random_number_generator_2 = np.random.normal(140, 15, 250);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.hist(random_number_generator, color = 'red', 
         edgecolor = 'black', label = 'Random Histogram');

axs.hist(random_number_generator_2, color = 'blue',
         edgecolor = 'black', label = 'Random Histogram 2')

plt.grid(color = 'grey', linestyle = '-.', linewidth = 0.5);
plt.legend();
plt.xlabel("Horizontal Label");
plt.ylabel("Vertical Label");
plt.show();







