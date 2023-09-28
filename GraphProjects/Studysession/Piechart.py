import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter

#Dataset
name = ["Mercedes", "AUDI", "BMW", "TESLA", "FORD"];

data = [45, 15, 10, 20, 5, 5];

explode = [0.5, 0.5, 0.5, 0.5, 0.5];

fig, axs = plt.subplots();
