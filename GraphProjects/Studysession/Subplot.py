import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5]);
y = np.array([10, 20, 30, 40, 50]);

plt.subplot(1,2, 1);
plt.plot(x, y);

x = np.array([]);
y = np.array([]);

plt.subplot();
plt.plot(x, y);

plt.show();