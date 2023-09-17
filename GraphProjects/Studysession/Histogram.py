import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

rand_number = np.random.normal(150, 20, 270);

plt.grid();
plt.hist(rand_number, color = 'red');
plt.legend()
plt.show();