#Second Visualization using matplotlib.
import numpy as np
import matplotlib.pyplot as plt

X_Data = np.random.random(1000) * 100
Y_Data = np.random.random(1000) * 100

# Visualizing with scatter plot.
plt.scatter(X_Data, Y_Data, c='#00f', marker="o", alpha=0.5)
plt.show()

# Visualizing with bar plot
x2_data = np.arange(10)
y2_data = np.random.uniform(0, 10, 10)

plt.bar(x2_data, y2_data)
plt.show()

# Visualizing with heatmap.
x3_data = np.random.uniform(0, 1, (8,8))
plt.imshow(x3_data)
plt.show()


# Visualizing contour plot.
x4_data = np.random.uniform(0, 1, (8,8))
plt.contourf(x4_data)
plt.show()

# Visualizing pie chart.
x5_data = np.random.uniform(0, 1, 4)
plt.pie(x5_data)
plt.show()


# Visualizing histogram:-
x6_data = np.random.normal(0, 1, 100)
plt.hist(x6_data)
plt.show()