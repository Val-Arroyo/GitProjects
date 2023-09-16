import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

random_number = np.random.normal(170, 10, 250);

print(random_number);

plt.grid();
plt.hist(random_number, color = 'blue', ec = 'red', lw = 1);
plt.legend();
plt.xlabel("Hundreds of Number");
plt.ylabel("Tens of Numbers");
plt.show();