"""
## Machine Learning and Data Visualization
This section introduces you to data visualization and basic machine learning concepts using 2D classification data.

**Question M3:** 
Fit two 2D Gaussian distributions to the points with label $l_i=0$ and $l_i=1$. For each class, calculate:
- The mean (centroid) of the points
- The covariance matrix

**Hint:** 
Use NumPy to calculate the mean and covariance. For class 0, filter points where `l == 0`, and for class 1, 
filter points where `l == 1`.
"""
 
from pathlib import Path
import numpy as np

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / r"data\data-2class.npz"

# Load the dataset
data = np.load(file_path)

# Extract points and labels
d = data['d']
l = data['l']

# Filter points by label
# Reshape labels if needed: l = l.flatten() or l = l.ravel()

points_class_0 = d[(l.flatten() == 0)]
points_class_1 = d[(l.flatten() == 1)]

# Calculate mean (centroid) for each class
mean_class_0 = np.mean(points_class_0, axis=0)
mean_class_1 = np.mean(points_class_1, axis=0)

# Calculate covariance matrix for each class
cov_class_0 = np.cov(points_class_0[0],points_class_0[1])
cov_class_1 =  np.cov(points_class_1[0],points_class_1[1])

print("Class 0:")
print(f"  Mean: {mean_class_0}")
print(f"  Covariance:\n{cov_class_0}")

print("\nClass 1:")
print(f"  Mean: {mean_class_1}")
print(f"  Covariance:\n{cov_class_1}")