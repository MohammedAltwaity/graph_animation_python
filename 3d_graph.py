import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
z = np.cos(x)

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Plot static 3D helix curve
ax.plot3D(x, y, z, color='purple', label='3D Helix')

# Animated point that moves along the helix
point, = ax.plot([], [], [], marker='o', color='red', markersize=8, label='Animated Point')

# Set axes limits and labels
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y = sin(x)')
ax.set_zlabel('Z = cos(x)')
ax.set_title("Animated 3D Helix with Moving Point")
ax.legend()

# Animation update function
def update(frame):
    point.set_data([x[frame]], [y[frame]])     # Update x and y data
    point.set_3d_properties([z[frame]])      # Update z data separately
    return point,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), interval=50, blit=True)

plt.show()
