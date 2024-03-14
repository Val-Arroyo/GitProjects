
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [20, 35, 30, 35, 27]
values2 = [25, 32, 34, 20, 25]
values3 = [30, 30, 25, 27, 20]

# Create a figure and 3D axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Calculate bottom positions for bars
bottom1 = np.zeros(len(categories))
bottom2 = np.array(values1)
bottom3 = np.array(values1) + np.array(values2)

# Plot bars for each group
for i, (bottom, values, color, label) in enumerate(zip([bottom1, bottom2, bottom3], [values1, values2, values3], ['r', 'g', 'b'], ['Group 1', 'Group 2', 'Group 3'])):
    ax.bar(categories, values, zs=i, zdir='y', color=color, alpha=0.8, label=label)

# Set labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Groups')
ax.set_zlabel('Values')
ax.set_title('Stacked Bar Graph in 3D')

# Add legend
ax.legend()

# Show plot
plt.show()