
# Task 2: Recursive Function - Factorial Utility

def factorial(n):

    # Check for negative numbers
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None

    # Base condition
    elif n == 0 or n == 1:
        return 1

    # Recursive condition
    else:
        return n * factorial(n - 1)


# Test the function
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))
