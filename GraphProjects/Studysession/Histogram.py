import matplotlib.pyplot as plt
import numpy as np

random_number = np.random.normal(170, 10, 250);

print(random_number);
plt.hist(random_number)
plt.show()