import matplotlib.pyplot as plt
import numpy as np

bleach = ["Ichigo", "Uryu Ishida", "Chad", "Inoue"];

y1 = np.array([]);
y2 = np.array([]);

plt.plot(bleach, y1, color = 'red', width = 0.4);
plt.plot(bleach, y2, bottom = y1, color = 'blue');

plt.xlabel("");
plt.ylabel("");
plt.title("Bleach Main Character Strength Levels per Arc");

plt.show();