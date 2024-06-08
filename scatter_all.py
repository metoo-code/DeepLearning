import pandas as pd
import matplotlib.pyplot as plt

# read_csv
file_path = 'Advertising2.csv'  
df = pd.read_csv(file_path)

# show_columns
print("Show DataFrame:")
print(df.columns)

#  'TV' & 'Sales' 
if 'TV' in df.columns and 'Sales' in df.columns:
    x = df['TV']
    y = df['Sales']

    #  scatter plot
    plt.scatter(x, y, c= 'red')

    #  labels & title
    plt.xlabel('TV')
    plt.ylabel('Sales')
    plt.title('Scatter Plot Advertising')

    # show
    plt.show()
else:
    print("error 'TV' / 'Sales'")
