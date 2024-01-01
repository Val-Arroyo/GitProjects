import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import style
from matplotlib import colors

plt.style.use("dark_background");

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 25.0, 10.0, 20.0];

fig, axs = plt.subplots(1, 1)

colors = ("grey", "blue", "red", "cyan");
explode = (0.1, 0.1, 0.1, 0.1);         

axs.pie(percent, labels = brands, colors = colors, 
        autopct = "%1.1f%%", explode = explode, shadow = True,
        wedgeprops = {"antialiased": True,
                      "linewidth": 3,
                      "edgecolor": "white"})
         
plt.grid()
plt.legend()
plt.axis("equal")
plt.show()