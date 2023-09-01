import matplotlib.pyplot as plt
import numpy as np

anime = ['One Piece', 'Naruto Shippuden','Bleach','Dragon Ball'];

y1 = np.array([20, 40, 15, 50]);
y2 = np.array([100, 80, 30, 30]);

plt.bar();

plt.title("Anime Popularity Chart Before and After");
plt.xlabel("Anime List");
plt.ylabel("Popularity Chart");

plt.show();