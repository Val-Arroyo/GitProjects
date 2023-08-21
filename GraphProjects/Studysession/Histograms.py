import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250);

plt.set_title("Random Histogram Sample");
plt.hist(x);
plt.show();