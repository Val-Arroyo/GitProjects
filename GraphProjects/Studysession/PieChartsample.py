import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors 
from matplotlib import style

brands = ["Apple"];
percent = [];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)

colors = ("grey", "blue", "white", "cyan")
style = (0.1, 0.1, 0.1, 0.1);

axs.pie(percent, labels = brands);