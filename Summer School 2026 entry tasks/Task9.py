"""
## Machine Learning and Data Visualization
This section introduces you to data visualization and basic machine learning concepts using 2D classification data.

**Question M1:**
Load the dataset from `data/data-2class.npz`. This file contains a set of 2-dimensional points `d` (shape: 1000x2),
and a corresponding set of labels `l` (shape: 1000x1). Create a 2D scatterplot of the points, using red for elements
with label 0, and blue for elements with label 1.

**Hint:**
Use matplotlib for plotting. The dataset keys are 'd' for data points and 'l' for labels.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / r"data\data-2class.npz"

# Load the dataset
data = np.load(file_path)

# Extract points and labels
d = data['d']
l = data['l']
x = d[:,0]
y = d[:,1]

# Create scatterplot
# Red for label 0, blue for label 1
plt.figure(figsize=(10,5))
plt.scatter(x,y,c=l,cmap='bwr_r')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Scatterplot of Data Points by Class')
plt.legend(['Class_0', 'Class_1'], loc='best')
plt.show()
plt.savefig('scatter_plot.png',dpi=300)
