import matplotlib.pyplot as plt
import numpy as np

year = np.array([1995, 2000, 2005, 2010, 2015, 2020, 2025]);
One_piece = np.array([20, 30, 50, 40, 60, 80, 100]);
Naruto = np.array([10, 30, 40, 50, 60, 70, 90]);
Bleach = np.array([0, 20, 40, 30, 65, 85, 95,]);
DragonBall = np.array([90, 100, 80, 75, 65, 40, 90]);

fig, ax = plt.subplots(2, 2);

ax[0, 0].plot(year, One_piece, color='red', marker="o", linewidth=2, sharex= True);
ax[0, 1].plot(year, Naruto, color='blue', marker="o", linewidth=2, sharex = True);
ax[1, 0].plot(year, Bleach, color='green', marker="o",linewidth=2, sharex = True);
ax[1, 1].plot(year, DragonBall, color='orange', marker="o", linewidth=2, sharex= True);

ax[0, 0].title.set_text("One Piece");
ax[0, 1].title.set_text("Naruto");
ax[1, 0].title.set_text("Bleach");
ax[1, 1].title.set_text("Dragon Ball");

plt.show();

