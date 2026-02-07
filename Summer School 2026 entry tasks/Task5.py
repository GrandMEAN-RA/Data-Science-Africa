"""
**Question E5:**
Check for missing values in the 'value' column. If there are any missing values,
replace them with the median value of that specific indicator_code. Display the
count of missing values before and after replacement.
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

# Check for missing values
missing_before = df_long['value'].isnull().sum()

print("Missing values before replacement:", missing_before)

# Replace missing values with median per indicator_code
df_long['value'] = df_long['value'].fillna(df_long.groupby('indicator_code')['value'].transform('median'))

missing_after = df_long['value'].isnull().sum()
print("Missing values after replacement:", missing_after)
