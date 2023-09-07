import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

A = np.array([20, 60, 40, 80, 120, 100, 160, 140]);
B = np.array([10, 30, 20, 40, 60, 50, 80, 70 ]);
X = np.arange(8);

plt.bar(X, A, color = 'maroon', alpha = 0.8);
plt.bar(X, -B, color = 'red', alpha = 0.8);

plt.grid();
plt.title("Positive and Negative Graph");
plt.xlabel("Numbers Display");
plt.ylabel("Positive and Negative Number Display");

plt
plt.show();