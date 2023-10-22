import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 25.0, 10.0, 20.0]

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

explode = (0.1, 0.1, 0.1, 0.1);
colors = ("grey", "blue", "white", "cyan");

axs.pie(percent, labels = brands, colors = colors,
        explode = explode, autopct = "%1.1f%%",
        shadow = True,
        wedgeprops = {"linewidth": 3,
                      "antialiased": True,
                      "edgecolor": "black"});

plt.legend();
plt.axis("equal");
plt.show();