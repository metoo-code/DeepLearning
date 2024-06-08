import pandas as pd
import matplotlib.pyplot as plt

# อ่านไฟล์ Excel
file_path = 'Advertising2.csv'  # แทนที่ด้วย path ของไฟล์ของคุณ
df = pd.read_csv(file_path)

# แสดงชื่อคอลัมน์ทั้งหมด
print("ชื่อคอลัมน์ใน DataFrame:")
print(df.columns)

# ตรวจสอบว่าคอลัมน์ 'TV' และ 'Sales' มีอยู่ใน DataFrame หรือไม่
if 'TV' in df.columns and 'Sales' in df.columns:
    x = df['TV']
    y = df['Sales']

    # สร้าง scatter plot
    plt.scatter(x, y)

    # เพิ่ม labels และ title
    plt.xlabel('TV')
    plt.ylabel('Sales')
    plt.title('Scatter Plot of TV Advertising vs Sales')

    # แสดงกราฟ
    plt.show()
else:
    print("คอลัมน์ 'TV' และ/หรือ 'Sales' ไม่พบในไฟล์ Excel")
