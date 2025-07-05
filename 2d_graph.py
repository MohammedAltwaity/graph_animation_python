import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)

# Static curve: sin(x)
y_static = np.sin(x)
ax.plot(x, y_static, label='sin(x)', color='blue')  # Static curve

# Animated marker
line, = ax.plot([], [], marker="o", markersize=10, color="red", label='animated point')

# Axes settings
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Sine Wave with Static Curve")
ax.legend()
ax.grid(True)

# Animation function
def update(frame):
    new_x = [x[frame]]
    new_y = [np.sin(x[frame])]
    line.set_data(new_x, new_y)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), interval=50, blit=True)

plt.show()
