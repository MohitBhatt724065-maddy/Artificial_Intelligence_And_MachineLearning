#Second Visualization using matplotlib.
import numpy as np
import matplotlib.pyplot as plt

X_Data = np.random.random(1000) * 100
Y_Data = np.random.random(1000) * 100

plt.scatter(X_Data, Y_Data, c='#00f', marker="*", alpha=0.5)
plt.show()