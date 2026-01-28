import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Read data from Excel file
data = pd.read_csv('Urban data.csv', encoding='utf-8')

# Extract location, population, and GDP as features
features = data[['longitude', 'latitude', 'GDP', 'The proportion of the tertiary industry']].values

# Normalize the location information
normalized_locations = (features[:, :2] - np.mean(features[:, :2], axis=0)) / np.std(features[:, :2], axis=0)

# Standardize the proportion of the tertiary industry and GDP
normalized_features = (features[:, 2:] - np.mean(features[:, 2:], axis=0)) / np.std(features[:, 2:], axis=0)

# Cluster based on location
location_clusters = 3  # Number of cluster centers
kmeans_location = KMeans(n_clusters=location_clusters, n_init=10)
location_labels = kmeans_location.fit_predict(normalized_locations)

# Use the location clustering result as new features
new_features = np.column_stack((normalized_features, location_labels))

# Cluster based on the new features
data_clusters = 3  # Number of cluster centers
kmeans_data = KMeans(n_clusters=data_clusters, n_init=10)
data_labels = kmeans_data.fit_predict(new_features)

# Add clustering results to the data
data['Clustering results'] = data_labels

# Write the results to an Excel file
data.to_csv('Urban Clustering Result.csv', index=False, encoding='utf-8')