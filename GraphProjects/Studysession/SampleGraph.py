import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors

brands = ["Apple", "Samsung"];
percentage = [65.0, 35.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

colors = ("grey", "blue");
explode = (0.1, 0.1)
axs.pie(percentage, labels = brands, shadow = True, autopct = "%1.1f%%",
        colors = colors, explode = explode,
        wedgeprops = {"edgecolor": "black",
                      "linewidth": 3,
                      "antialiased": True} );
axs.set_title("")

plt.show();