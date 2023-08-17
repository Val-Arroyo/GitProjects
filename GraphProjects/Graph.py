import matplotlib.pyplot as plt
import numpy as py

#Variables between anime viewership per year

year = [2000, 2005, 2010, 2015, 2020, 2025];
One_piece = [10, 20, 30, 40, 50, 100];
Naruto = [5, 10, 15, 20, 25, 30];
Bleach = [15, 30, 40, 50, 60, 70];
DragonBall = [20, 40, 60, 80, 100, 90];

plt.plot(year, One_piece, color='orange', label='One Piece', marker='H');
plt.plot(year, Naruto, color='yellow', label='Naruto and Shippuden', marker='H');
plt.plot(year, Bleach, color='black', label='Bleach', marker='H');
plt.plot(year, DragonBall, color='blue', label='Dragon Ball', marker='H');

plt.xlabel("Years");
plt.ylabel("Viewership per Year");

plt.title("Anime Viewership for 2 Decades");

plt.legend();
plt.show();