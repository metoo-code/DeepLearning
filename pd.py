import pandas as pd

data = {
    'Name': ['John','Anna','Peter','Linda'],
    'Age': [28, 35, 40, 25],
    'City':['New York', 'Paris', 'London', 'Sydney']
}
df = pd.DataFrame(data)
print("DataFrame ເດີມໆ:")
print(df)

df['Age'] = df['Age'] + 1
print("\nDataFrames ແກ້ໄຂແລ້ວ:")
print(df)

new_data = {
    'Name': ['Mike','Emily'],
    'Age': [32, 29],
    'City': ['Berlin', 'Tokyo']
}
new_df = pd.DataFrame(new_data)

merged_df = pd.concat([df, new_df], ignore_index=True)
print("\nDataFrames ຫຼັງລວມແລ້ວ")
print(merged_df)

filtered_df = merged_df[merged_df['Age'] > 30]
print("\nDataFrames ຫຼັງານກຣອງ")
print(filtered_df)

print("\nສະຖິຕິ")
print(merged_df['Age'].describe)

