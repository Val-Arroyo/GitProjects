import matplotlib.pyplot as plt
import numpy as np

A = np.array([10, 20, 30, 40, 50, 60, 70, 80])
B = np.array([20, 40, 60, 80, 100, 120, 140, 160])
X = np.arange(8)

plt.barh(X, B, color = 'red', alpha = 0.8,);
plt.barh(X, -A, color = 'blue', alpha = 0.8 );

plt.grid();
plt.xlabel("Positive and Negative Label", size = 10);
plt.ylabel("Range Label", size = 10);
plt.title("Graph Sample");
plt.show();