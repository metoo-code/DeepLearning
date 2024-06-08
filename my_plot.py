import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
file_path = r'Advertising1.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Assuming the Excel file has columns named 'X' and 'Y'
x = df['X'].values
y = df['Y'].values

# Create scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot from Excel Data')

# Show plot
plt.show()
