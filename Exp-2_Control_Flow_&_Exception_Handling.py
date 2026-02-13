try:
    # Accept three numbers
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    # Control flow to find maximum
    if a >= b and a >= c:
        print("Maximum number:", a)
    elif b >= a and b >= c:
        print("Maximum number:", b)
    else:
        print("Maximum number:", c)

except ValueError:
    print("Error: Invalid input! Please enter integer values only.")
