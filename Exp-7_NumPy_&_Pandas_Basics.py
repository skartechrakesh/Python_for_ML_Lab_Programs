import numpy as np
import pandas as pd

# Accept number of elements
n = int(input("Enter number of elements: "))

# Accept elements from user
elements = []
for i in range(n):
    value = float(input(f"Enter element {i+1}: "))
    elements.append(value)

# Create NumPy array
arr = np.array(elements)

print("\nNumPy Array:")
print(arr)

# Convert to Pandas DataFrame
df = pd.DataFrame(arr, columns=["Values"])

print("\nPandas DataFrame:")
print(df)

# Calculate basic statistics
print("\nBasic Statistics")
print("----------------")
print("Sum:", df["Values"].sum())
print("Mean:", df["Values"].mean())
print("Minimum:", df["Values"].min())
print("Maximum:", df["Values"].max())
print("Standard Deviation:", df["Values"].std())
