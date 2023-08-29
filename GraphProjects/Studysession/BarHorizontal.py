import matplotlib.pyplot as plt
import numpy as np

y = ["One", "Two", "Three", "Four", "Five"];

x = [35, 20, 15, 25, 40];

plt.barh(y, x, color = 'maroon');

plt.ylabel("Pen Sold");
plt.xlabel("Price");
plt.title("Horizontal Bar Graph");

plt.show();