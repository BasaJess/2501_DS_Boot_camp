import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.animation import FuncAnimation, PillowWriter

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data points for two classes
class_1 = np.random.randn(50, 3) + np.array([2, 2, 2])
class_2 = np.random.randn(50, 3) + np.array([-2, -2, -2])

# Combine the data
data = np.vstack((class_1, class_2))
labels = np.array([0]*50 + [1]*50)


from sklearn.neighbors import KNeighborsClassifier

# Initialize KNN with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(data, labels)


# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot class 1 points
ax.scatter(class_1[:, 0], class_1[:, 1], class_1[:, 2], c='b', label='Class 1')

# Plot class 2 points
ax.scatter(class_2[:, 0], class_2[:, 1], class_2[:, 2], c='r', label='Class 2')

# Set plot labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()



import matplotlib.animation as animation

# New data point to classify
new_point = np.array([[0, 0, 0]])

# Predict the class of the new point
predicted_class = knn.predict(new_point)[0]

# Find the k-nearest neighbors
distances, indices = knn.kneighbors(new_point)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot
def update(num):
    ax.clear()
    ax.scatter(class_1[:, 0], class_1[:, 1], class_1[:, 2], c='b', label='Class 1')
    ax.scatter(class_2[:, 0], class_2[:, 1], class_2[:, 2], c='r', label='Class 2')
    ax.scatter(new_point[:, 0], new_point[:, 1], new_point[:, 2], c='g', label='New Point', s=100)

    # Draw lines to the k-nearest neighbors
    for i in range(num):
        neighbor_index = indices[0][i]
        neighbor = data[neighbor_index]
        ax.plot([new_point[0, 0], neighbor[0]], [new_point[0, 1], neighbor[1]], [new_point[0, 2], neighbor[2]], 'k--')

    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Target')
    ax.legend()
    ax.set_title(f'KNN Classification (k={num})')

ani = animation.FuncAnimation(fig, update, frames=3, interval=1000, repeat=False)
plt.show()

writer = PillowWriter(fps=10)
ani.save('knn_animation.gif', writer=writer)


plt.rcParams['animation.ffmpeg_path'] = '/path/to/ffmpeg'
ani.to_html5_video()
