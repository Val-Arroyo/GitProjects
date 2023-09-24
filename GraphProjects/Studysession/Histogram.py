import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

Hist_1 = np.random.randn(300, 1);
Hist_2 = np.random.randn(200, 1);

fig, axs = plt.subplots(1, 1,);