import matplotlib.pyplot as plt
import numpy as np

A = np.array([4, 2, 3]);
B = np.array([]);
X = np.arrange(6);

plt.barh(X, A, color = 'red');
plt.barh(X,  -B, color = 'blue');
plt.title("Back To Back Graph Sample");

plt.grid();
plt.show();