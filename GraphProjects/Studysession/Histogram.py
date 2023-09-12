import matplotlib as plt
import numpy as np

rand = np.random.normal(170, 10, 250);

print(rand);

plt.hist(rand);

plt.show();