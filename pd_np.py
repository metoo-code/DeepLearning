import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# โหลดข้อมูลจากไฟล์ CSV ด้วย Pandas
data = pd.read_csv('data.csv')

# แปลงข้อมูลเป็น Numpy array
numpy_array = data.to_numpy()

# คำนวณค่าเฉลี่ยของแต่ละคอลัมน์
mean_values = np.mean(numpy_array, axis=0)

# คำนวณค่าเบี่ยงเบนมาตรฐานของแต่ละคอลัมน์
std_values = np.std(numpy_array, axis=0)

# กรองข้อมูลเฉพาะกลุ่มที่ตรงตามเงื่อนไขด้วย Pandas
filtered_data = data[data['column_name'] == 'condition']

# วิเคราะห์ความสัมพันธ์ระหว่างตัวแปรด้วย Numpy
correlation_matrix = np.corrcoef(numpy_array)

# สร้างกราฟแท่งเปรียบเทียบค่าเฉลี่ยของกลุ่มข้อมูลด้วย Pandas
data.groupby('column_name').mean().plot(kind='bar')

# แสดงกราฟ
plt.show()

'''''
# การสร้างภาพข้อมูล
import matplotlib.pyplot as plt
plt.hist(merged_df['Age'], bins=3, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()
'''