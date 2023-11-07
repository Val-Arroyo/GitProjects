import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors 
from matplotlib import style

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 25.0, 10.0, 20.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)