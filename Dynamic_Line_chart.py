import matplotlib.pyplot as plt
import numpy as np

x = int(input("Enter values for x axis"))
y = int(input("Enter values for y axis"))

x= np.array(x)
y= np.array(y)

plt.plot(x, y, marker='o')

plt.title("Simple Dynamic Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
