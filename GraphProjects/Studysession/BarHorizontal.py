import matplotlib.pyplot as plt
import numpy as np

x = ['Java', 'Python', 'C', 'C++', 'Javascript'];
y1 = [30, 50, 10, 20, 40];
y2 = [35, 55, 15, 25, 45];

plt.bar(x, y1, color = 'r');
plt.bar(x, y2, bottom = y1, color = 'b');
plt.show();