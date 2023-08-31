import matplotlib.pyplot as plt
import numpy as np

anime = ['One Piece','Naruto Shippuden','Bleach', 
         'Dragon Ball', 'Death Note'];

y1 = np.array([40, 30, 20, 50, 10]);
y2 = np.array([100, 60, 40, 20, 30]);

plt.bar(anime, y1, color = 'maroon');
plt.bar(anime, y2, bottom = y1, color = 'red');

plt.xlabel();
plt.ylabel();
plt.legend();
plt.title();

plt.show();