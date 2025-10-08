# Matplotlib Visualization Examples – Scatter, Bar, and Heatmap
# Demonstrates: scatter plot, bar plot, and image visualization using random data.

import numpy as np
import matplotlib.pyplot as plt

# Create a Figure with 3 Axes (3 rows, 1 column)
fig, ax = plt.subplots(3, 1, figsize=(6, 8))

# ---- 1. Scatter Plot ----
X = np.random.uniform(0, 1, 100)  # 100 random X values between 0 and 1
Y = np.random.uniform(0, 1, 100)  # 100 random Y values between 0 and 1
ax[0].scatter(X, Y, color='orange', edgecolors='black')
ax[0].set_title("Scatter Plot")
ax[0].grid(True)

# ---- 2. Bar Plot ----
X = np.arange(10)  # X positions (0 to 9)
Y = np.random.uniform(1, 10, 10)  # 10 random heights between 1 and 10
ax[1].bar(X, Y, color='orange', edgecolor='black')
ax[1].set_title("Bar Plot")
ax[1].grid(True)

# ---- 3. Image / Heatmap ----
Z = np.random.uniform(0, 1, (8, 8))  # 8x8 matrix of random values between 0 and 1
im = ax[2].imshow(Z, cmap='Oranges', interpolation='nearest')
ax[2].set_title("Image (Heatmap)")

# Adjust layout for better spacing
plt.tight_layout()

# Display all the plots together
plt.show()
