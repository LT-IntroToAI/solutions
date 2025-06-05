import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#imports the data
data = pd.read_csv("part5-unsupervised-learning/old_faithful_data.csv")
data = data[["eruptions", "waiting"]]

#standardizes the data
scaler = StandardScaler().fit(data)
x_std = scaler.transform(data)

x_orig = x_std * scaler.scale_ + scaler.mean_
#sets the value of k and creates kmeans model
k = 2
km = KMeans(n_clusters=k).fit(x_std)

#returns centroid x, y values in a 2D array
centroids = km.cluster_centers_
print(centroids)
new_centroid = centroids * scaler.scale_ + scaler.mean_
#returns the cluster labels of each data point in the x_std data set
labels = km.labels_
print(labels)

#sets the size of the scatterplot
plt.figure(figsize=(10,8))

#plots the data points for each cluster
for i in range(k):
    cluster = x_orig[labels == i]
    plt.scatter(cluster[:,0], cluster[:,1])

#plots the centriods
plt.scatter(new_centroid[:, 0], new_centroid[:, 1], marker='X', s=100,
            c='r', label='centroid')

#labels the axes
plt.xlabel('Length of Eruption (minutes)')
plt.ylabel('Time Between Eruptions(minutes)')
plt.show()