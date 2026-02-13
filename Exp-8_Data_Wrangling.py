import pandas as pd

# Accept CSV file name from user
file_name = input("Enter CSV file name (with .csv): ")

# Read CSV file
df = pd.read_csv(file_name)

print("\nOriginal DataFrame:")
print(df)

# Handle missing values (replace with column mean)
df_filled = df.fillna(df.mean(numeric_only=True))

print("\nDataFrame after handling missing values:")
print(df_filled)

# Accept new column names from user
print("\nEnter new column names")
new_columns = {}
for col in df_filled.columns:
    new_name = input(f"Rename column '{col}' to: ")
    new_columns[col] = new_name

# Rename columns
df_renamed = df_filled.rename(columns=new_columns)

print("\nDataFrame after renaming columns:")
print(df_renamed)
