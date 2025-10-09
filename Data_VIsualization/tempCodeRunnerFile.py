# Matplotlib Basic Visualization for Scatter, Bar, and Heatmap.
import numpy as np
import matplotlib.pyplot as plt
fig , ax= plt.subplots()
x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

ax.scatter(x_data, y_data)
plt.show()

x1_data = np.arange(10)
x2_data = np.random.uniform(0, 10, 10)
ax.bar(x1_data, x2_data)
plt.show()

x2_data = np.random.uniform(0, 1, (8,8))
ax.imshow(x2_data)
plt.show()