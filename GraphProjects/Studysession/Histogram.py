import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors

graph1 = np.random.randn(500, 1);
graph2 = np.random.randn(400, 1);
graph3 = np.random.randn(300, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.hist(graph1, color = 'red', edgecolo = 'black');
axs.hist(graph2, color = 'blue', edgecolor = 'black');
axs.hist(graph3, color = 'green', edgecolor = 'black');

plt.show();