import matplotlib.pyplot as plt
import numpy as np

A = np.array([4, 2, 3, 6, 1, 5]);
B = np.array([2, 4, 6, 3, 2, 5]);
X = np.arange(6);

plt.barh(X, A, color = 'red', width = 0.5);
plt.barh(X,  -B, color = 'blue', width = 0.5);
plt.title("Back To Back Graph Sample");

plt.grid();
plt.show();