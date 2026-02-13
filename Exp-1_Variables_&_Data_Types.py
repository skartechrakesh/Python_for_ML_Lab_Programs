# Accept two numbers from the user
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Display data types
print("Data type of num1:", type(num1))
print("Data type of num2:", type(num2))

# Type conversion
num1_float = float(num1)
num2_int = int(num2)

print("num1 after converting to float:", num1_float)
print("num2 after converting to int:", num2_int)

# Memory management
print("Memory location of num1:", id(num1))
print("Memory location of num2:", id(num2))
