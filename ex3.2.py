import pandas as pd

# 1. Create DataFrame & add column
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
})
df['Salary'] = [50000, 60000, 75000, 48000, 55000]
print("DataFrame:\n", df)

# 2. Access, Filter & Sort
print("\nName Column:\n", df['Name'])
print("\nAge > 30:\n", df[df['Age'] > 30])
print("\nSorted by Age:\n", df.sort_values(by='Age', ascending=False))

# 3. Aggregations & Groupby
print("\nAverage Age:", df['Age'].mean())
print("\nAvg Salary by City:\n", df.groupby('City')['Salary'].mean())

# 4. Apply, Drop & CSV I/O
df['Age_Sq'] = df['Age'] ** 2
df.drop(columns=['Age_Sq'], inplace=True)
df.to_csv('output.csv', index=False)
print("\nRead from CSV:\n", pd.read_csv('output.csv'))
