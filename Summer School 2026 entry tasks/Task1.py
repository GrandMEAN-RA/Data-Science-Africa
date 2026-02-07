"""
##Data Analysis 
**Question E1:**
Load the Uganda Consumer Price Index dataset from the file `
data/uganda-consumer-price-index-trends-2020-2023.xlsx` into a pandas dataframe.
Display the first 10 rows and the shape of the dataframe.
"""

from pathlib import Path
import pandas as pd

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / r"data\uganda-consumer-price-index-trends-2020-2023.xlsx"

# Load the Uganda CPI dataset
df = pd.read_excel(file_path)

# Display first 10 rows and shape
print("Shape of dataframe:", df.shape)
print("\nFirst 10 rows: \n", df.head(10))
print(...)
