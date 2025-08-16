import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Sample Documents (Replace with real data)
documents = [
    "Machine learning is a subset of artificial intelligence.",
    "Deep learning is a type of machine learning.",
    "Python is a programming language widely used in AI.",
    "AI applications are transforming industries.",
    "Data science involves statistics and machine learning.",
    "Neural networks are powerful for deep learning.",
    "Big data is crucial for analytics.",
    "Cloud computing enables scalable data storage.",
    "Blockchain technology is used for secure transactions.",
    "Cybersecurity is important for protecting digital assets."
]

# Step 1: Convert documents to TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(documents)

# Step 2: Apply K-Means Clustering
num_clusters = 3  # You can change the number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Step 3: Reduce Dimensions for Visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())

# Step 4: Plot the clusters
plt.figure(figsize=(8, 6))
for i in range(num_clusters):
    plt.scatter(X_pca[labels == i, 0], X_pca[labels == i, 1], label=f'Cluster {i}')
    
plt.xlabel("PCA Feature 1")
plt.ylabel("PCA Feature 2")
plt.title("K-Means Clustering on TF-IDF Features")
plt.legend()
plt.show()

# Step 5: Print cluster assignments
df = pd.DataFrame({'Document': documents, 'Cluster': labels})
print(df)
