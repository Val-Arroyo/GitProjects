import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd 
from matplotlib.ticker import 

brands = ["Apple", "Samsung"];
percent = [65, 35];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

colors = ("grey", "blue");
explode = (0.1, 0.1);

axs.pie(percent, labels = brands, colors = colors, shadow = True,
        autopct= "%1.1f%%", explode = explode,
        wedgeprops = {"linewidth": 3,
                      "edgecolor": "black",
                      "antialiased": True})

plt.legend();
plt.show();
