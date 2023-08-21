import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250);

plt.set_title("Random");
plt.hist(x);
plt.show();