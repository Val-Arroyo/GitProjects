import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from numpy.lib.histograms import histogram

rand_number = np.random.randn(500, 1);
fig = plt.figure(figsize=(8, 5));

plt.grid();
plt.hist(rand_number, color = 'red', edgecolor = 'blue', label = 'Histogram');
plt.legend([''])
plt.show();