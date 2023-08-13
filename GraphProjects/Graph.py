import matplotlib.pyplot as plt
import numpy as np


ax = plt.axes();
#plot 1:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
y = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]);

plt.subplot(1, 3, 1);
plt.figure(facecolor="red");
plt.plot(x,y ,color = 'red', marker = '*');
plt.xlabel("Money Income");
plt.ylabel("Yearly Income");
plt.title("SALES");

#plot 2:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

plt.subplot(1, 3, 2);   
plt.figure(facecolor="green");
plt.plot(x,y, color = 'blue', marker = "*");
plt.xlabel("Money Income");
plt.ylabel("Yearly Income");
plt.title("INCOME");

#plot 3:
x = np.array([0, 10, 20, 30, 40]);
y = np.array([10000, 30000, 50000, 20000, 60000]);

plt.subplot(1, 3, 3);
plt.figure("")
plt.plot(x, y, color = 'black', marker = '*');
plt.xlabel("Investments return");
plt.ylabel("Yearly income");
plt.title("Investments");

plt.suptitle("MONEY GRAPHS");
plt.show();