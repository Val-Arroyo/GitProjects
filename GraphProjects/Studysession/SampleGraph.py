import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.histograms import histogram

series1 = np.random.randn(500, 1);
series2 = np.random.randn(400, 1);  


plt.hist(series1, label='series1', alpha=.8, edgecolor='red')
 

plt.hist(series2, label='series2', alpha=0.7, edgecolor='yellow')
plt.legend()

plt.show()
plt.show()