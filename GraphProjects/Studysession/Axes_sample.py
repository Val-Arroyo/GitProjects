import matplotlib.pyplot as plt
import numpy as np

year = np.array([1995, 2000, 2005, 2010, 2015, 2020, 2025]);
One_piece = np.array([20, 30, 50, 40, ]);
Naruto = np.array([]);

fig, ax = plt.subplots();

ax.plot(year, One_piece);
ax.plot(year, Naruto);

