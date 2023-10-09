import matplotlib as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

brands = ["Apple", "Samsung"];
percentage = [65, 35];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);