# Working on dataset visualization on different indicators or features.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Datasets/Housing.csv')
print(dataset.head())


x_data = dataset['area']
y_data = dataset['price']

plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price')

#plt.scatter(x_data, y_data, c='#00f', marker = "*", alpha=0.5)
plt.plot(x_data, y_data)
 
plt.show()