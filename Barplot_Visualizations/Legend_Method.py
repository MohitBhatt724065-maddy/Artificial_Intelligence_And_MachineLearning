# Understanding how the legend(_) method in matplotlib works for visualization.
import matplotlib.pyplot as plt
import random

Standard = [1 + x for x in range(10)]
Female = [random.randint(10, 50) for _ in range(10)]
Male = [random.randint(10, 50) for _ in range(10)]


plt.bar(Standard, Female, label='Female')
plt.bar(Standard, Male, label='Male')
plt.xlabel('Standard')
plt.ylabel('Weight')
plt.title('Weight vs Standard')
plt.legend()
plt.show()