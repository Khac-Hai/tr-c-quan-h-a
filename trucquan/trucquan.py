import numpy as np
import matplotlib.pyplot as plt

height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

plt.bar(y_pos, height, color="teal")

plt.xticks(y_pos, bars)

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.title("Example 1", fontsize=15)

plt.savefig('example1.pdf')
plt.show()