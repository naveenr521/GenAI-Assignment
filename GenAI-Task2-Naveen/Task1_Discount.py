# Task 1: Discount Rules

# Get order amount from user
try:
    order_amount = int(input("Enter your order amount: "))

    # Apply discount rules
    if order_amount >= 2000:
        discount = 15

    elif order_amount >= 1500:
        discount = 10

    elif order_amount >= 1000:
        discount = 7

    else:
        discount = 0

    # Calculate discount and final amount
    discount_amount = order_amount * discount / 100
    final_amount = order_amount - discount_amount

    # Display results
    print("Order Amount:", order_amount)
    print("Discount:", discount, "%")
    print("Discount Amount:", discount_amount)
    print("Final Amount:", final_amount)

except ValueError:
    print("Error: Please enter a valid numeric amount.")