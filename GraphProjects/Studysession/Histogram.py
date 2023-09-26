import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter
from numpy.lib.histograms import histogram

random_number_generator = np.random.normal(170, 15, 250);

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.hist(random_number_generator);