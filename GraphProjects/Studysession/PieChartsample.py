import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 35.0, 10.0, 20.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)

colors = ("grey", "blue", "red", "white");
explode = (0.1, 0.1, 0.1, 0.1);

axs.pie(percent, labels = brands, shadow = True, autopct = "%1.1f%%",
        colors = colors, explode = explode,
        wedgeprops = {"edgecolor": "black",
                      "antialiased": True,
                      "linewidth": 3})
plt.legend()
plt.axis("equal")
plt.show();