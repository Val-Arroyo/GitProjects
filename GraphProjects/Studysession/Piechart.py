import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter

#Dataset
name = ["Mercedes", "AUDI", "BMW", "TESLA", "FORD"];

data = [45, 15, 10, 20, 10];

Explode = [0.1, 0.1, 0.1, 0.1, 0.1];

fig, axs = plt.subplots(1, 1, figsize = (7, 5));

axs.pie(data, labels = name, explode = Explode, edgecolor = 'black');

plt.show();
