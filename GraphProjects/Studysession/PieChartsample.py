import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [55.0, 25.0, 5.0, 15.0 ];

fig, axs, = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.pie()