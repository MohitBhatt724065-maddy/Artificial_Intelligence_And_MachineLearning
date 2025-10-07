# Creating a simple plot using python special functions.
import numpy as np
import matplotlib.pyplot as plt
import random

x_data = [2006 + x for x in range (15)]
y_data = [random.randint(50,90) for _ in range (15)] # Since we use _ instead of x because we dont't want a loop but we want to repeat it 15 times.

print(x_data, y_data)

'''plt.scatter(x_data, y_data, c='#00f', marker="*", alpha=0.5)
plt.show()'''
plt.xlabel('Year')
plt.ylabel('Weight')
plt.title('Weight vs Year')
plt.plot(x_data, y_data)
plt.show()

