import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))  

plt.plot(x, y1, color='blue', linestyle='--', linewidth=2, marker='o', markersize=5, label='Sine')
plt.plot(x, y2, color='red', linestyle='-', linewidth=2, marker='x', markersize=5, label='Cosine')

plt.title("Customized Line Chart", fontsize=16, fontweight='bold', color='purple')
plt.xlabel("X-axis", fontsize=12, color='green')
plt.ylabel("Y-axis", fontsize=12, color='green')

plt.grid(True, linestyle=':', linewidth=1, color='gray')

plt.legend(fontsize=12, loc='upper right')

plt.xlim(0, 10)
plt.ylim(-1.2, 1.2)

plt.show()
