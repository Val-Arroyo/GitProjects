import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5, 6, 7, 4] 
bins = [1, 2, 3, 4, 5, 6, 7]

fig = plt.figure(figsize = (8, 5));

plt.hist(x, bins);

plt.title("Histogram");

plt.legend(["bar"]);

plt.show();