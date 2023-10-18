import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 35.0, 10.0, 20.0];

fig, axs = plt.subplots()