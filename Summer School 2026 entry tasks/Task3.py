"""
**Question E3:**
Convert the 'date' column to datetime format. Handle the date format appropriately
(e.g., 'dec-20' should become '2020-12-01', 'jan-21' should become '2021-01-01', etc.).
"""

from pathlib import Path
import pandas as pd

BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / r"data\uganda-consumer-price-index-trends-2020-2023.xlsx"

# Load the Uganda CPI dataset
df = pd.read_excel(file_path)

# Reshape dataframe from wide to long format
df_long = pd.melt(df, id_vars=['indicator_code', 'description'], var_name='date')

# Convert date column to datetime
df_long['date'] = pd.to_datetime(df_long['date'], format='%b-%y')

print("Date column info:")
print(df_long['date'].head(10))
print("\nDate range:", df_long['date'].min(), "to", df_long['date'].max())
