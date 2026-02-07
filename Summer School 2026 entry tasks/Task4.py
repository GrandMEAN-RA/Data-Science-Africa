"""
**Question E4:**
Filter the dataframe to include only CPI indicators (indicator_code starting with 'CPI_').
Create separate dataframes for:
- All Items CPI (CPI_16 and CPI_09)
- Core CPI (CPI_CORE_16 and CPI_CORE_09)
- Food CPI (CPI_FOOD_16 and CPI_FOOD_09)
- Energy Fuel and Utilities CPI (CPI_EFU_16 and CPI_EFU_09)
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

# Filter for CPI indicators
df_cpi = (df_long[df_long['indicator_code'].isin(['CPI_16', 'CPI_09', 'CPI_CORE_16', 'CPI_CORE_09',
          'CPI_FOOD_16', 'CPI_FOOD_09', 'CPI_EFU_16','CPI_EFU_09'])])

# Create separate dataframes
df_all_items = df_cpi[df_cpi['indicator_code'].isin(['CPI_16', 'CPI_09'])]
df_core = df_cpi[(df_cpi['indicator_code'] == 'CPI_CORE_16') | (df_cpi['indicator_code'] == 'CPI_CORE_09')]
df_food = df_cpi[(df_cpi['indicator_code'] == 'CPI_FOOD_16') | (df_cpi['indicator_code'] =='CPI_FOOD_09')]
df_efu = df_cpi[df_cpi['indicator_code'].isin(['CPI_EFU_16','CPI_EFU_09'])]

print("All Items CPI shape:", df_all_items.shape)
print("Core CPI shape:", df_core.shape)
print("Food CPI shape:", df_food.shape)
print("EFU CPI shape:", df_efu.shape)
