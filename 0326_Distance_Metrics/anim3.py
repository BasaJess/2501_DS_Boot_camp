import numpy as np
from sklearn.datasets import make_classification

# Generate synthetic 3D data
X, y = make_classification(n_samples=100, n_features=3, n_informative=3, n_redundant=0, random_state=42)

from sklearn.neighbors import KNeighborsClassifier

# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

import plotly.express as px

# Create a DataFrame for Plotly
import pandas as pd
df = pd.DataFrame(X, columns=['X1', 'X2', 'X3'])
df['Class'] = y

# Create an interactive 3D scatter plot
fig = px.scatter_3d(df, x='X1', y='X2', z='X3', color='Class', title='3D KNN Visualization')

# Save the figure as an HTML file
fig.write_html('knn_interactive_plot.html')
