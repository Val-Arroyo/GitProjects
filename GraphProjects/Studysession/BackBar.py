import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

data = {"Name": ["Alex", "Bob", "Clarein", "Dexter"],
        "Marks": [45, 23, 78, 65]}
 
df = pd.DataFrame(data, columns=['Name', 'Marks'])
 
plt.figure(figsize=(8, 8))
 
plots = sns.barplot(x="Name", y="Marks", data=df)
 
for bar in plots.patches:
   
  
  plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')
 

plt.xlabel("Students", size=14)
 
plt.ylabel("Marks Secured", size=14)
 
plt.title("This is an annotated barplot")
 

plt.show()