import matplotlib.pyplot as plt
import numpy as np

y = np.array([50, 25, 15, 10]);
mylabels = ["A", "B", "C", "D"];
myexplode = [0.2, 0.2, 0.2, 0.2];

plt.pie(y, labels= mylabels, explode=myexplode, shadow= True);
plt.legend(title = "Grades");
plt.show();