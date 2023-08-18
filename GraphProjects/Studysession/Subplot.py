import matplotlib.pyplot as plt
import numpy as np

x=np.array([1, 2, 3, 4, 5])
 
# making subplots
fig, ax = plt.subplots(3, 2)
 
# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)
ax[2, 0].plot(x, x*x*x*x);
ax[2, 1].plot();
 
# set the title to subplots
ax[0, 0].title.set_text("Linear")
ax[0, 1].title.set_text("Double")
ax[1, 0].title.set_text("Square")
ax[1, 1].title.set_text("Cube")
ax[2, 0].title.set_text("Random");
 
# set spacing
fig.tight_layout()
plt.show()

