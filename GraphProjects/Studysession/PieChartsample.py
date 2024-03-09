import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors


brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 25.0, 10.0, 20.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)

colors = ("grey", "blue", "red", "cyan");
explode = (0.1, 0.1, 0.1, 0.1);         

axs.pie(percent, labels = brands, colors = colors, explode = explode, 
        autopct = "%1.1f%%", startangle = 0, shadow = True,
        wedgeprops = {"linewidth": 3,
                      "edgecolor": "black",
                      "antialiased": True});

axs.set_title("Phone Brand Percentage")
      
plt.grid()
plt.legend()
plt.axis("equal")
plt.show()