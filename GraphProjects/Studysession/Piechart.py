import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

phone_brands = ["Apple", "Samsung", "Oppo", "Oneplus", "Xiaomi"];
phone_data = [45, 15, 10, 20, 10];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

colors = ["Grey", "Blue", "Cyan", "Black"];

axs.pie(phone_brands, phone_data, );