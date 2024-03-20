import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create some sample data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
y2 = np.cos(x) + np.random.normal(0, 0.1, 100)
data = pd.DataFrame({'x': x, 'y1': y1, 'y2': y2})

# Plot 1: Scatter plot using Matplotlib
plt.subplot(221)  # 2 rows, 2 columns, plot number 1
plt.scatter(data['x'], data['y1'])
plt.title('Scatter Plot (Matplotlib)')
plt.xlabel('x')
plt.ylabel('y1')

# Plot 2: Line plot using Seaborn
plt.subplot(222)  # 2 rows, 2 columns, plot number 2
sns.lineplot(data=data, x='x', y='y2')
plt.title('Line Plot (Seaborn)')
plt.xlabel('x')
plt.ylabel('y2')

# Plot 3: Histogram using Pandas
plt.subplot(223)  # 2 rows, 2 columns, plot number 3
data['y1'].plot(kind='hist')
plt.title('Histogram (Pandas)')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot 4: Box plot using Seaborn
plt.subplot(224)  # 2 rows, 2 columns, plot number 4
sns.boxplot(data=data[['y1', 'y2']], orient='v')
plt.title('Box Plot (Seaborn)')
plt.ylabel('Value')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()