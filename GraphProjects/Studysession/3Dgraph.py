import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Plot a simple scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.title('Simple Scatter Plot')
plt.show()
