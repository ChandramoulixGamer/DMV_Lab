import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 100)

line, = ax.plot(x, np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x + frame))
    return line,

animation = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100),
                          interval=50)

plt.title("Animated Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
