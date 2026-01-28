# Carbon-Emission-Prediction-Based-on-LSTM
### For Urban Clustering.py
It utilizes the K-means clustering algorithm to perform clustering analysis on urban data. It first reads the data from a CSV file, extracts features such as longitude, latitude, GDP, and the proportion of the tertiary industry. These features are then normalized to have zero mean and unit variance. The algorithm clusters the data based on location information and combines the clustering results with the normalized features. Finally, the script assigns cluster labels to each data point and writes the results to a new CSV file. K-means clustering works by iteratively assigning data points to the nearest cluster centroid and updating the centroids based on the mean of the assigned points until convergence.
### For Carbon Emission Prediction Model.ipynb
This is the code for a carbon emission prediction model. The code can directly read TIFF images and train a model between X (land use in 2015, GDP in 2015, carbon emissions in 2015, population in 2015) and Y (carbon emissions in 2020). The aim is to use landuse, GDP, carbon emissions, and population data from the current year to predict carbon emissions five years later.

To link to this article: https://doi.org/10.1080/17538947.2024.2405541
