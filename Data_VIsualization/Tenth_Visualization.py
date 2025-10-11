# Understanding error and box plot.
import numpy as np
import matplotlib.pyplot as plt

x_data = np.arange(5)
y_data = np.random.uniform(0, 1, 5)
print(x_data)
print(y_data)

fig, ax = plt.subplots()
ax.errorbar(x_data, y_data, y_data/4)
plt.show()
z= np.random.normal(0, 1, (100, 3))
ax.boxplot(z)
plt.show()

