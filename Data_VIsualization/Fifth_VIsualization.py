# Understanding the structure-Figure and Axes.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Dataset = pd.read_csv('Datasets/Housing.csv')
print(Dataset.sample(10))
print(Dataset.size)

sample_data = Dataset.sample(25)

# Creating a figure and one axes.
fig, ax = plt.subplots()

# ax.scatter(sample_data['area'], sample_data['price'], c='#00f', marker="*", alpha=0.5)

ax.plot(sample_data['area'], sample_data['price'], linestyle='dashed',marker='o')
ax.set_xlabel('Area')
ax.set_ylabel('Price')
ax.set_title('Area vs Price')

plt.show()


    