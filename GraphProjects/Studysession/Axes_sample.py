import matplotlib.pyplot as plt
import numpy as np

year = np.array([1995, 2000, 2005, 2010, 2015, 2020, 2025]);
One_piece = np.array([20, 30, 50, 40, 60, 80, 100]);
Naruto = np.array([10, 30, 40, 50, 60, 70, 90]);
Bleach = np.array([0, 20, 40, 30, 65, 85, 95,]);

fig, ax = plt.subplots();

ax.plot(year, One_piece, marker='o', label='One Piece');
ax.plot(year, Naruto, marker='o', label='Naruto');
ax.plot(year, Bleach, marker='o', label='Bleach');

plt.title("Anime Popularity Chart");
plt.ylabel("Popularity Chart");
plt.xlabel("Years");
plt.legend();
plt.grid();
plt.show();
