# First Basic Bar Plot Visualization.
import matplotlib.pyplot as plt
import random
x_data = [2000 + x for x in range(10)]
y_data = [random.randint(50,90) for _ in range(10)]


plt.bar(x_data, y_data)
plt.xlabel('Year')
plt.ylabel('Weight')
plt.title('Weight vs Year') 
plt.show()