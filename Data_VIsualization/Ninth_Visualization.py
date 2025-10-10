# Plotting standard visualization on osciallting sin waves compared to eighth visualization.
import numpy as np
import matplotlib.pyplot as plt

x1_data = np.linspace(0, 10, 50)
y1_data = 4 + 1 * np.sin(2 * x1_data)

x2_data = np.linspace(0, 10, 25)
y2_data = 4 + 1 * np.sin(2 * x2_data)

# Plot
fig, ax = plt.subplots()

ax.plot(x2_data, y2_data + 2.5, 'x', markeredgewidth = 2)
ax.plot(x1_data, y1_data, linewidth = 2)
ax.plot(x2_data, y2_data - 2.5, 'o-', linewidth = 2)

ax.set(xlim=(0, 8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1, 8))

plt.show()