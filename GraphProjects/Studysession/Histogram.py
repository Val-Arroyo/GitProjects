import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

np.random.seed(23685752);
N_points = 10000;
n_bins = 20;

x = np.random.randn(N_points);
y = .8 ** x + np.random.randn(10000) + 25

fig, axs = plt.subplots(1, 1, figsize = (10, 7).)