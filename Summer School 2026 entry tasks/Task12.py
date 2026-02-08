"""
## Machine Learning and Data Visualization
This section introduces you to data visualization and basic machine learning concepts using 2D classification data.

**Question M4:** 
Create a heatmap plotting the two Gaussian distributions and superimpose a scatterplot of the data points.

**Hint:**
- Use `scipy.stats.multivariate_normal` to create the Gaussian distributions
- Create a meshgrid for the heatmap
- Use `plt.contour()` or `plt.contourf()` for the heatmap
- Overlay the scatterplot on top
"""

from pathlib import Path
from scipy.stats import multivariate_normal
import numpy as np
import matplotlib.pyplot as plt

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / r"data\data-2class.npz"

# Load the dataset
data = np.load(file_path)

# Extract points and labels
d = data['d']
l = data['l']

# Create meshgrid for heatmap
x_min, x_max = d[:, 0].min() - 1, d[:, 0].max() + 1
y_min, y_max = d[:, 1].min() - 1, d[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))

# Filter points by label
# Reshape labels if needed: l = l.flatten() or l = l.ravel()

points_class_0 = d[(l.flatten() == 0)]
points_class_1 = d[(l.flatten() == 1)]

# Calculate mean (centroid) for each class
mean_class_0 = np.mean(points_class_0, axis=0)
mean_class_1 = np.mean(points_class_1, axis=0)

# Calculate covariance matrix for each class
cov_class_0 = np.cov(points_class_0, rowvar=False)
cov_class_1 = np.cov(points_class_1, rowvar=False)

# Create Gaussian distributions
gaussian_class_0 = multivariate_normal(mean=mean_class_0, cov=cov_class_0)
gaussian_class_1 = multivariate_normal(mean=mean_class_1, cov=cov_class_1)

# Calculate probability density for each point in meshgrid
pos = np.dstack((xx, yy))
pdf_class_0 = gaussian_class_0.pdf(pos) # Calculate PDF over the entire meshgrid
pdf_class_1 = gaussian_class_1.pdf(pos) # Calculate PDF over the entire meshgrid

# Create heatmap (contour plot)
fig, ax = plt.subplots(figsize=(10, 8))
ax.contourf(xx, yy, pdf_class_0, cmap='Reds', alpha=0.5)
ax.contourf(xx, yy, pdf_class_1, cmap='Blues', alpha=0.5)

# Superimpose scatterplot
ax.scatter(d[:, 0], d[:, 1], c=l, cmap='bwr_r', s=10, alpha=0.8, zorder=2) # zorder to ensure scatter is on top

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Gaussian Distributions Heatmap with Data Points')
plt.savefig("Super-imposed plots", dpi=300)
plt.show()