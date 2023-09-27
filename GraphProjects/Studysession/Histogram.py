import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

random_number_1 = np.random.normal(240, 10, 240);
random_numner_2 = np.random.normal(140, 10, 240);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)