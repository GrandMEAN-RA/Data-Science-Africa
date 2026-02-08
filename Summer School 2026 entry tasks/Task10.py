"""
## Machine Learning and Data Visualization
This section introduces you to data visualization and basic machine learning concepts using 2D classification data.

**Question M2:**
Draw a straight line separating the two classes on the scatterplot. The line should visually separate the red points
(label 0) from the blue points (label 1). You can choose the line parameters (slope and intercept) manually - the
purpose is to think about how this line could be used to classify the data.

**Hint:**
You can use `plt.plot()` or `plt.axline()` to draw a line. Think about where the line should be positioned to best
separate the two classes.
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

# Draw a separating line
# You can choose the line parameters (slope and intercept)
# Example: plt.axline((x1, y1), slope=m) or plt.plot([x1, x2], [y1, y2])
x1 = -2
y1 = 8
x2 = 8
y2 = -2

#plt.figure(figsize=(10,5))
#plt.scatter(x,y,c=l,cmap='bwr_r')
plt.plot([x1, x2], [y1, y2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Scatterplot with Separating Line')
plt.legend(['Class 0', 'Class 1', 'Separating Line'])
plt.savefig('scatter_plot.png',dpi=300)
plt.show()


