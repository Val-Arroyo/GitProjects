import matplotlib.pyplot as plt
import numpy as np

X = ["A", "B", "C", "D"];
Y = [1, 2, 3, 4];

plt.barh(X, Y);

for index, value, in enumerate(Y):
    plt.text(value, index, str(value));

plt.show();