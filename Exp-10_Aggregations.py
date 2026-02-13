import pandas as pd

# Accept CSV file name from user
file_name = input("Enter CSV file name (with .csv): ")

# Read CSV file
df = pd.read_csv(file_name)

print("\nOriginal Dataset")
print("----------------")
print(df)

# Accept categorical column for grouping
group_column = input("\nEnter column name to group by: ")

# Perform aggregations
grouped_data = df.groupby(group_column).agg(
    Total=('Sales', 'sum'),
    Average=('Sales', 'mean'),
    Minimum=('Sales', 'min'),
    Maximum=('Sales', 'max')
)

print("\nAggregated Data")
print("----------------")
print(grouped_data)
