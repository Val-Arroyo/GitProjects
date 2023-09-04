import matplotlib.pyplot as plt
import numpy as np

A = np.array([40, 30, 20, 10, 60, 70, 50, 80]);
B = np.array([80, 60, 40, 20, 120, 140, 100, 160]);
X = np.arange(8);

plt.barh(X, A, color = 'red');
plt.barh(X, -B, color = 'blue');

plt.grid();
plt.xlabel();
plt.ylabel();
plt.title();
plt.show();