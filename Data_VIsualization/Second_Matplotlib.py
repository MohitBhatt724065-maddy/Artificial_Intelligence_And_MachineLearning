# Basic visualization on line plot.

import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(0, 10*np.pi, 1000)
y_data = np.sin(x_data)

plt.plot(x_data, y_data)
plt.show(  )