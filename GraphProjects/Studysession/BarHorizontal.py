import matplotlib.pyplot as plt
import numpy as np

anime = ['One Piece','Naruto Shippuden','Bleach', 
         'Dragon Ball', 'Death Note'];

y1 = np.array([40, 30, 20, 50, 10]);
y2 = np.array([100, 60, 40, 20, 30]);

plt.bar(anime, y1, color = 'blue');
plt.bar(anime, y2, bottom = y1, color = 'red');

plt.xlabel("Anime List ");
plt.ylabel("Popularity Chart");
plt.legend(["One Piece"]);
plt.title("Anime Popularity");

plt.show();