import matplotlib.pyplot as plt
import numpy as np

x = int(input("Enter values for x"))
y = int(input("Enter values for y"))

x = np.array(x)
y = np.array(y)

plt.scatter(x, y, color='blue', marker='o')

plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.show()