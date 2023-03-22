import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create some data
x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
z = x**2 + y**2

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the surface plot
surf = ax.plot_surface(x, y, z, cmap='coolwarm', alpha=0.8)

# Define the vertices of the polygon
verts = [
    [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
    [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)],
    [(0, 0, 0), (0, 0, 1), (1, 0, 1), (1, 0, 0)],
    [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)],
    [(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)],
    [(0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
]

# Define the faces of the polygon
faces = Poly3DCollection(verts, alpha=0.5, facecolors='r')

# Add the polygon to the plot
ax.add_collection3d(faces)

# Show the plot
plt.show()