import matplotlib.pyplot as plt
import numpy as np

series1 = np.random.randn(500, 1);
series2 = np.random.randn(400, 1);  

plt.hist(series1, color = 'red');
plt.hist(series2, color = 'blue');

plt.show()