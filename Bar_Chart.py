import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]


plt.bar(categories, values, color='skyblue', edgecolor='black')


plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
