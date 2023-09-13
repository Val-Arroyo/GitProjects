import matplotlib.pyplot as plt
from matplotlib import colors
from 
import numpy as np
import pandas as pd
import seaborn as sns

random_number = np.random.normal(170, 10, 250);

print(random_number);
plt.hist(random_number);
plt.show();