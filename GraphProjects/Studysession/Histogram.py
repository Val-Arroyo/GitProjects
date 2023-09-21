import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

graph_1 = np.random.randn(100, 1);
graph_2 = np.random.randn(50, 1);

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.hist();
axs.hist();

