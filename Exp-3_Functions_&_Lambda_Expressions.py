# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Accept input from user
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))

# Lambda function to filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers from the list:", even_numbers)
