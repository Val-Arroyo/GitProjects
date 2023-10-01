import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib import colors 

brands = ["Apple", "Samsung", "Oneplus", "Xiaomi"];

percent = [45, 35, 15, 5];

fig, axs = subplots(1, 1, figsize = (7, 5), tight_layout = True);

Explode = (0.1, 0.1, 0.1, 0.1)