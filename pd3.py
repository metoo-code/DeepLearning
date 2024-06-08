import pandas as pd

# Read the Excel file
file_path = r'Advertising1.xlsx'  # Replace with your file path
df = pd.read_excel(file_path, engine='openpyxl')  # Specify the engine

# Display the first few rows of the dataframe
print(df.head())
