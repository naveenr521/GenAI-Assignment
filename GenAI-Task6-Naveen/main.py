# ==========================================
# TASK 1: SAFE DIVISION UTILITY
# ==========================================

print("\n========== TASK 1: SAFE DIVISION ==========")

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Division Result:", result)

finally:
    print("Operation Complete")


# ==========================================
# TASK 2: BILL CALCULATOR WITH ERROR HANDLING
# ==========================================

print("\n========== TASK 2: BILL CALCULATOR ==========")

prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:

    try:
        # Check whether the price is a number
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")

        # Check whether the price is negative
        if price < 0:
            raise ValueError("Negative price not allowed")

        # Add valid price to total
        if price == 0:
            print("Skipping zero price")
            continue

        total += price

    except TypeError as e:
        print("Type Error:", e)

    except ValueError as e:
        print("Value Error:", e)

    else:
        print("Valid price:", price)
        print("Running Total:", total)

print("Final Bill Total:", total)


# ==========================================
# TASK 3: CUSTOM EXCEPTION - AGE VALIDATOR
# ==========================================

print("\n========== TASK 3: AGE VALIDATOR ==========")

def check_age(age):

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    return age


try:
    age = int(input("Enter your age: "))

    check_age(age)

    print("Valid Age:", age)

except ValueError as e:
    print("Error:", e)


# ==========================================
# TASK 4: FILE READER WITH EXCEPTION HANDLING
# ==========================================

print("\n========== TASK 4: FILE READER ==========")

try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:

        lines = file.readlines()

        print("First 3 lines of the file:")

        for line in lines[:3]:
            print(line, end="")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("\nFile operation attempted.")


# ==========================================
# TASK 5: MINI PROGRAM - SAFE SHOPPING CART
# ==========================================

print("\n========== TASK 5: SAFE SHOPPING CART ==========")

cart = []

while True:

    user_input = input(
        "Enter product price (or 'q' to finish): "
    )

    # Stop when user enters q
    if user_input.lower() == 'q':
        break

    try:
        # Convert input into a number
        price = float(user_input)

        # Raise custom ValueError for negative price
        if price < 0:
            raise ValueError("Negative price not allowed")

        # Add valid price to cart
        cart.append(price)

        print("Price added successfully.")

    except ValueError as e:

        if str(e) == "Negative price not allowed":
            print("Error:", e)
        else:
            print("Invalid input. Please enter a number.")

# Calculate total bill
total_bill = sum(cart)

print("\nShopping Cart Summary")
print("Total Items:", len(cart))
print("Total Bill:", total_bill)
