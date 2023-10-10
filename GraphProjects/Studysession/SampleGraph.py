import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors

brands = ["Apple", "Samsung"];
percentage = [65.0, 35.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

axs.pie(percentage, labels = brands, shadow = True);

plt.show();