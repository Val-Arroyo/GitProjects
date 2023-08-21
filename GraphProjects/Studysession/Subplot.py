import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5]);
y = np.array([10, 20, 30, 40, 50]);

plt.subplot(1, 2, 1);
plt.plot(x, y, linestyle="dashed", color="");

x = np.array([50, 60, 70, 80, 90, 100]);
y = np.array([10, 40, 20, 30, 50, 60]);

plt.subplot(1, 2, 2);
plt.plot(x, y, linestyle="dashed");

plt.show();