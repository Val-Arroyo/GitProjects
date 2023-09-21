import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplot

graph_1 = np.random.randn(100, 1);
graph_2 = np.random.randn(50, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.hist(graph_1, color = 'red');
axs.hist(graph_2, color = 'blue');

plt.grid(color = 'red', linestyle = '-.', linewidth = 0.6);
plt.legend()
plt.show();