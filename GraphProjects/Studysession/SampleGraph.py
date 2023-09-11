import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter 
import numpy as np
import seaborn as sns
import pandas as pd

a = np.array([20, 15, 30, 40, 10, 25]);

fig, ax = plt.subplots(figsize = (10, 7));

ax.hist(a, );