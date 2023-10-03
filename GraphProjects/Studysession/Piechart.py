import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors

brands = ["Apple", "Samsung", "OnePlus", "Oppo"];
sales = [45.0, 25.0, 15.0, 15.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

Space = (0.1, 0.1, 0.1, 0.1);
colors = ("grey", "blue", "white", "cyan");

axs.pie(sales, labels = brands, shadow = True, explode = Space,
        colors = colors, autopct='%1.1f%%')

plt.show();