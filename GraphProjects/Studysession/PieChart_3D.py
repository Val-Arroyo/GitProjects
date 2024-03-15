import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20]

# Create a 3D-like effect by plotting labels
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Pie chart parameters
explode = (0, 0, 0, 0, 0.1)  # explode the last slice
colors = plt.cm.tab10(np.arange(len(labels)))  # color palette

# Plot pie chart slices and labels
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

# Draw a circle at the center of the pie to make it look like a donut chart
center_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(center_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Set title
plt.title('3D-like Pie Chart')

# Show plot
plt.show()
