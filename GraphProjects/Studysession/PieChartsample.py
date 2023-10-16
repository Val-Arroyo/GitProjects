import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [35.0, 30.0, 10.0, 25.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

colors = ("grey", "blue", "white", "cyan")
explode = (0.1, 0.1, 0.1, 0.1)
axs.pie(percent, labels = brands, shadow = True, autopct = "%1.1f%%",
        colors = colors, explode = explode
        wedgeprops = {"linewidth": 3,
                     "edgecolor": "black",
                     "antialiased": True} );


plt.show();