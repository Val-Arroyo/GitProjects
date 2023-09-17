import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

rand_number = np.random.randn(500, 1);

plt.grid();
plt.hist(rand_number, color = 'red', edgecolor = 'blue');
plt.legend()
plt.show();