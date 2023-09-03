import matplotlib.pyplot as plt
import numpy as np

A = np.array([4, 2, 3, 6, 1, 5]);
B = np.array([2, 4, 6, 3, 2, 5]);
X = np.arange(6);

plt.barh(X, A, color = 'red', linewidth = 0.04);
plt.barh(X,  -B, color = 'blue', linewidth = 0.4);
plt.title("Back To Back Graph Sample");

plt.grid();
plt.show();