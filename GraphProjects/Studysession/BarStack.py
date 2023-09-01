import matplotlib.pyplot as plt
import numpy as np

anime = ['One Piece', 'Naruto Shippuden','Bleach','Dragon Ball'];

y1 = np.array([20, 40, 15, 50]);
y2 = np.array([100, 80, 30, 30]);

plt.bar(anime, y1, color = 'blue');
plt.bar(anime, y2, bottom = y1, color = 'red', width = 0.4);

plt.title("Anime Popularity Chart Before and After");
plt.xlabel("Anime List");
plt.ylabel("Popularity Chart");

plt.show();