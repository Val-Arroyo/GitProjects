import matplotlib.pyplot as plt
import numpy as np

x = ['Java', 'Python', 'C', 'C++', 'Javascript'];
y1 = [10, 60, 30, 20, 40];
y2 = [20, 100, 60, 40, 80];

plt.bar(x, y1, color = 'red');
plt.bar(x, y2, bottom = y2, color = 'blue');
plt.show();