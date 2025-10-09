# Visualizing different kinds of graph.

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x1_data = np.random.random(50) * 100
y1_data = np.random.random(50) * 100

ax.scatter(x1_data, y1_data)
plt.show()