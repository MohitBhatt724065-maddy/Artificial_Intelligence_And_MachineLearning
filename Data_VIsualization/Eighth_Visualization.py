# plotting y versus x as line and/or markers.

import numpy as np
import matplotlib.pyplot as plt


plt.style.use('_mpl-gallery')

# make data
x1_data = np.linspace(0, 10, 100)
y_data = 4 + 1 * np.sin(2 * x1_data)

x2_data = np.linspace(0, 10, 25)
y2_data = 4 + 1 * np.sin(2 * x2_data)

# plot
fig, ax = plt.subplots()


ax.plot(x1_data, y_data)
ax.plot(x2_data, y2_data, 'o')

plt.show()