import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, y1, color='blue')
ax1.set_title("Sine Wave")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")

ax2.plot(x, y2, color='red')
ax2.set_title("Cosine Wave")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")

plt.tight_layout()  
plt.show()
