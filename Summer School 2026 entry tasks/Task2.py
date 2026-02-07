"""
**Question E2:**
Reshape the dataframe from wide format to long format.
The monthly columns (dec-20, jan-21, etc.) should become a single 'date' column,
and their values should be in a 'value' column. The resulting dataframe should have
columns: 'indicator_code', 'description', 'date', and 'value'.
"""

from pathlib import Path
import pandas as pd

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / r"data\uganda-consumer-price-index-trends-2020-2023.xlsx"

# Load the Uganda CPI dataset
df = pd.read_excel(file_path)

# Reshape dataframe from wide to long format
df_long = pd.melt(df, id_vars=['indicator_code', 'description'], var_name='date')

print("Shape after reshaping:", df_long.shape)
print("\nFirst 10 rows: \n")
print(df_long.head(10))
