# Using Data From Dataset For Visualization.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Datasets/Housing.csv')
print(dataset)

x_data = dataset['area']
y_data = dataset['price']

fig , ax = plt.subplots()

ax.scatter(x_data, y_data)
plt.show()