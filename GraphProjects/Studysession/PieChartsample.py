import matplotlib.pyplot as plt
import numpy as np


plt.style.use("dark_background");

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [45.0, 25.0, 10.0, 20.0];

fig, axs = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True)

colors = ("grey", "blue", "red", "cyan");
explode = (0.1, 0.1, 0.1, 0.1);         

axs.pie(percent, labels = brands, colors = colors, explode = explode,
        autopct = "%1.1f%%", shadow = True, startangle = 0, 
        wedgeprops = {"edgecolor": "black",
                      "linewidth": 3, 
                      "antialiased": True})
      
plt.grid()
plt.legend()
plt.axis("equal")
plt.show()