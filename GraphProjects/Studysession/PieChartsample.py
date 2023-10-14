import matplotlib.pyplot as plt
import numpy 

brands = ["Apple", "Samsung", "Google", "OnePlus"];
percent = [55.0, 25.0, 5.0, 15.0 ];

fig, axs, = plt.subplots(1, 1, figsize = (7, 5), tight_layout = True);

colors = ("grey", "blue", "red", "purple")
explode = (0.1, 0.1, 0.1, 0.1);

axs.pie(percent, labels = brands, explode = explode,
        colors = colors, shadow = True, autopct = "%1.1f%%",
        wedgeprops = {"edgecolor": "black",
                      "linewidth": 2,
                      "antialiased": True});

plt.grid();
plt.legend();
plt.show();