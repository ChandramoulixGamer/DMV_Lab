import matplotlib.pyplot as plt
import numpy as np

x= np.array([0,20,40,60,80,100])
y= np.array([64,68,79,39,50,60,20,10,59,33])

plt.hist(y,bin=x, edgecolor = "block")

plt.show()
