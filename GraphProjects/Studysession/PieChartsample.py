import matplotlib.pyplot as plt
import numpy as np      
import pandas as pd
import seaborn as sns
from matplotlib.ticker import PercentFormatter
from matplotlib import colors
from matplotlib import style

plt.style.use("dark_background");

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 25.0, 10.0, 20.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)

colors = ("grey", "blue", "red", "cyan");
explode = (0.1, 0.1, 0.1, 0.1);         

axs.pie(percent)
      
plt.grid()
plt.legend()
plt.axis("equal")
plt.show()