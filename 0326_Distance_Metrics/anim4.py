import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier

# Generate a 3D dataset
X, y = make_classification(n_samples=100, n_features=3, n_informative=3, n_redundant=0, random_state=42)

# Train a KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Create a mesh grid for plotting decision boundaries
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
z_min, z_max = X[:, 2].min() - 1, X[:, 2].max() + 1
xx, yy, zz = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100),
                         np.linspace(z_min, z_max, 100))

# Flatten the mesh grid
grid_points = np.c_[xx.ravel(), yy.ravel(), zz.ravel()]

# Create a function to update the plot with a new point
def create_frame(new_point):
    # Append the new point to the dataset
    X_new = np.vstack([X, new_point])
    y_new = np.append(y, knn.predict([new_point])[0])

    # Re-train the KNN classifier with the new point
    knn.fit(X_new, y_new)

    # Predict the class for each point in the mesh grid
    Z = knn.predict(grid_points)
    Z = Z.reshape(xx.shape)

    # Create the surface plot
    surface = go.Surface(x=xx, y=yy, z=zz, surfacecolor=Z, colorscale='Viridis', opacity=0.5)

    # Create the scatter plot for the data points
    scatter = go.Scatter3d(x=X_new[:, 0], y=X_new[:, 1], z=X_new[:, 2],
                           mode='markers', marker=dict(color=y_new, size=5))

    # Create the new point to be added
    new_point_scatter = go.Scatter3d(x=[new_point[0]], y=[new_point[1]], z=[new_point[2]],
                                     mode='markers', marker=dict(color='red', size=10))

    # Return the data for the frame
    return [surface, scatter, new_point_scatter]

# Create frames for the animation
frames = [go.Frame(data=create_frame([np.random.uniform(x_min, x_max),
                                      np.random.uniform(y_min, y_max),
                                      np.random.uniform(z_min, z_max)]),
                   name=f'Frame {i}') for i in range(1, 11)]
