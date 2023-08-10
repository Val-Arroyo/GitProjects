import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([3, 8, 1, 10, 4, 1, 7, 6, 4, 5, 2 ]);

plt.subplot(1, 2, 1)
plt.plot(x,y ,color = 'red', marker = 'o');
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50, 60, 70,])

plt.subplot(1, 2, 2)
plt.plot(x,y, color = 'blue', marker = "o");
plt.title("INCOME");

plt.show();