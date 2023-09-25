import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

random_number = np.random.normal(150, 10, 270);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.hist();