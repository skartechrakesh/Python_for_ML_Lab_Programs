import pandas as pd
import matplotlib.pyplot as plt

# Accept CSV file name from user
file_name = input("Enter CSV file name (with .csv): ")

# Read CSV file
df = pd.read_csv(file_name)

print("\nDataset")
print("--------")
print(df)

# Scatter Matrix
print("\nDisplaying Scatter Matrix...")
pd.plotting.scatter_matrix(df, figsize=(8, 8))
plt.show()

# Accept column name for time series analysis
column_name = input("\nEnter column name for time series plotting: ")

# Lag Plot
print("Displaying Lag Plot...")
pd.plotting.lag_plot(df[column_name])
plt.show()

# Autocorrelation Plot
print("Displaying Autocorrelation Plot...")
pd.plotting.autocorrelation_plot(df[column_name])
plt.show()
