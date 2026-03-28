import matplotlib.pyplot as plt
import numpy as np

x= int(input("Enter Valuies for x"))
y= int(input("Enter Valuies for x"))

x= np.array(x)
y= np.array(y)

plt.hist(y,bin=x,edgecolor = 'black')

plt.show()
