import matplotlib.pyplot as plt
import numpy as np

A = np.array([]);
B = np.array([]);
X = np.arrange(6);

plt.barh(X, A, color = 'red');
plt.barh(X,  -B, color = 'blue');
plt.title("Back to Back Graph Sample");

plt.show();