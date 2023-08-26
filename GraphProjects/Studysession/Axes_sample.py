import matplotlib.pyplot as plt
import numpy as np

year = np.array([1995, 2000, 2005, 2010, 2015, 2020, 2025]);
One_piece = np.array([20, 30, 50, 40, 60, 80, 100]);
Naruto = np.array([10, 30, 40, 50, 60, 70, 90]);
Bleach = np.array([0, 20, 40, 30, 65, 85, 95,]);
DragonBall = np.array([90, 100, 80, 75, 65, 40, 90]);

fig, ax = plt.subplots();

ax.plot(year, One_piece, marker='o', label='One Piece', linewidth=2);
ax.plot(year, Naruto, marker='o', label='Naruto', linewidth=2);
ax.plot(year, Bleach, marker='o', label='Bleach', linewidth=2);
ax.plot(year, DragonBall, marker='o', label='Dragon Ball', linewidth=2);

plt.title("Anime Popularity Chart");
plt.ylabel("Popularity Chart");
plt.xlabel("Years");
plt.legend(loc='upper right');
plt.grid();
plt.show();
