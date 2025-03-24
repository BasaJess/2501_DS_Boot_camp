import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.animation import FuncAnimation, PillowWriter

# Generate synthetic 3D data
X, y = make_classification(n_samples=100, n_features=3, n_informative=3, n_redundant=0, random_state=42)


# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis')

# Function to update the plot for animation
def update(frame):
    ax.cla()  # Clear the current axes
    ax.set_title(f'Frame {frame}')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Class')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis')
    ax.scatter(X[frame, 0], X[frame, 1], X[frame, 2], c='red', s=100, label='Current Point')
    ax.legend()

# Create an animation
ani = FuncAnimation(fig, update, frames=len(X), interval=200)

# Save the animation as a GIF
writer = PillowWriter(fps=10)
ani.save('knn_animation.gif', writer=writer)
