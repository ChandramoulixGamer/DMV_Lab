import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 15, 13, 17, 20, 18, 25, 22]

plt.scatter(x, y, color='blue', marker='o')

plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.show()
