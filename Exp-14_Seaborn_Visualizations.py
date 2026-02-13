import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Accept CSV file name
file_name = input("Enter CSV file name (with .csv): ")

# Read dataset
df = pd.read_csv(file_name)

print("\nDataset")
print("--------")
print(df)

# Heatmap (Correlation Matrix)
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
print("Displaying Pair Plot...")
sns.pairplot(df)
plt.show()

# Accept columns for regression plot
x_col = input("Enter X-axis column for regression plot: ")
y_col = input("Enter Y-axis column for regression plot: ")

# Regression Plot
plt.figure(figsize=(6, 4))
sns.regplot(x=x_col, y=y_col, data=df)
plt.title("Regression Plot")
plt.show()
