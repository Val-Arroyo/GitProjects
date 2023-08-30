import matplotlib.pyplot as plt
import numpy as np

x = ['Java', 'Python', 'C', 'C++', 'Javascript'];
y1 = [10, 20, 10, 20, 30];
y2 = [15, 25, 15, 25, 35];

plt.bar(x, y1, color = 'r');
plt.bar(x, y2, bottom = y2, color = 'b');
plt.show();