import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors

brands = ["Apple", "Samsung"];
percentage = [65, 35];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

explode = (0.1, 0.1);
colors = ("grey", "blue");

axs.pie(percentage, labels = brands, colors = colors, explode = explode,
        shadow = True, autopct = "%1.1f%%",
        wedgeprops = {"linewidth": 2,
                      "edgecolor": "black",
                      "antialiased": True})

plt.axis('equal');
plt.show();
















