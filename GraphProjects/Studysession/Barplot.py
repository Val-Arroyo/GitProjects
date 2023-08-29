import matplotlib.pyplot as plt
import numpy as np

data = np.array['One Piece': 80, 'Naruto': 25, 'Bleach': 20, 'Dragon Ball':50 ];

anime = list(data.keys());
values = list(data.values());

fig = plt.figure(figsize = (10, 5));

plt.bar(anime, values, color = 'red', width = 0.4);

plt.xlabel("Anime");
plt.ylabel("Popularity Chart");
plt.title("Anime Popularity Chart");

plt.show();