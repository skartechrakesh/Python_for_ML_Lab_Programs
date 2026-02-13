import pandas as pd

# Accept CSV file name from user
file_name = input("Enter CSV file name (with .csv): ")

# Read CSV file
df = pd.read_csv(file_name)

print("\nOriginal DataFrame")
print("------------------")
print(df)

# Accept column name to modify
column_name = input("\nEnter column name to apply function: ")

# Define custom function
def increase_value(x):
    return x * 1.10   # Increase value by 10%

# Apply function to the column
df[column_name] = df[column_name].apply(increase_value)

print("\nDataFrame after applying custom function")
print("---------------------------------------")
print(df)
