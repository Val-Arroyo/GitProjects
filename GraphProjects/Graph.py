import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
y = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]);

plt.subplot(1, 2, 1)
plt.plot(x,y ,color = 'red', marker = 'o');
plt.title("SALES");

#plot 2:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

plt.subplot(1, 2, 2);   
plt.plot(x,y, color = 'blue', marker = "o");
plt.title("INCOME");

#plot 3:

x = np.array([]);

plt.show();