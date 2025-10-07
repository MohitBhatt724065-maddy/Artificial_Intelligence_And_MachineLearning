# Plotting a simple sine curve using matplotlib.
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(0, 10*np.pi, 1000)
y_data = np.sin(x_data)

fig, ax = plt.subplots()

ax.plot(x_data, y_data)
plt.show()

# print(np.pi)

print(len(x_data))