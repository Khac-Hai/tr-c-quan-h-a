import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

bars1=[12, 30, 1, 8, 22]
bars2=[28, 6, 16, 5, 10]
bars3=[29, 3, 24, 25, 17]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, bars1, color='lightseagreen',
        width=barWidth, edgecolor='white', label='var1')
plt.bar(r2, bars2, color='teal',
        width=barWidth, edgecolor='white', label='var2')
plt.bar(r3, bars3, color='darkslategrey',
        width=barWidth, edgecolor='white', label='var3')

plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], [ 'A', 'B', 'C', 'D', 'E'])
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.title("Example 2", fontsize=15)
plt.legend()

plt.savefig('example2.pdf')
plt.show()