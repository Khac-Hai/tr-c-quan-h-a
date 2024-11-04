import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bars1=[12, 28, 1, 8, 22]
bars2=[28, 7, 16, 4, 10]
bars3=[25, 3, 23, 25, 17]

bars = np.add(bars1, bars2).tolist()
r=[0,1,2,3,4]

name = ['A','B','C','D','E']
barWidth = 0.75

plt.bar(r, bars1, color='darkslategrey',edgecolor='white',
        width=barWidth, label='var1')
plt.bar(r, bars2, bottom=bars1, color='teal',edgecolor='white',
        width=barWidth, label='var2')
plt.bar(r, bars3, bottom=bars, color='lightseagreen',
        edgecolor='white', width=barWidth, label='var3')

plt.legend()
plt.xticks(r, name)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.title("Example 3", fontsize=15)


plt.savefig('example3.pdf')
plt.show()