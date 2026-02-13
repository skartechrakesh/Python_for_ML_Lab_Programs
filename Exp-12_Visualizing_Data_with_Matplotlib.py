import matplotlib.pyplot as plt

# Accept number of data points
n = int(input("Enter number of data points: "))

x = []
y = []

print("Enter X and Y values:")
for i in range(n):
    x_val = int(input(f"X[{i+1}]: "))
    y_val = int(input(f"Y[{i+1}]: "))
    x.append(x_val)
    y.append(y_val)

# Line Graph
plt.figure()
plt.plot(x, y, marker='o')
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Graph")
plt.legend(["Line Plot"])
plt.show()

# Bar Chart
plt.figure()
plt.bar(x, y)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.legend(["Bar Plot"])
plt.show()

# Pie Chart
plt.figure()
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
