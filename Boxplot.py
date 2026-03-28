import matplotlib.pyplot as plt
weights = [25,28,29,29,30,34,35,35,37,38]
plt.boxplot(weights)
plt.xlabel('Weights(grams)')
plt.ylabel("Number of Boxes")
plt.title("BOXPLOT")
plt.show()