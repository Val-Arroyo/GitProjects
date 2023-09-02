import matplotlib.pyplot as plt
import numpy as np

bleach = ["Ichigo", "Uryu Ishida", "Chad", "Inoue"];

y1 = np.array([40, 30, 20, 10]);
y2 = np.array([100, 90, 50, 40]);

plt.plot(bleach, y1, color = 'red', width = 0.4);
plt.plot(bleach, y2, bottom = y1, color = 'blue', width = 0.4);

plt.xlabel("Character Name");
plt.ylabel("Strength Level");
plt.title("Bleach Main Character Strength Levels per Arc");

plt.show();