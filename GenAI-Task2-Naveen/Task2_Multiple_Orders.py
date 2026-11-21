
# Task 2: Process Multiple Orders (for loop)

# Given order amounts
orders = [1200, 2500, 800, 1750, 3000]

# Initialize total revenue and discounted order count
total_revenue = 0
discounted_orders = 0

print("Order Amount | Discount | Final Amount")
print("----------------------------------------")

# Process each order
for order_amount in orders:

    # Apply discount rules
    if order_amount >= 2000:
        discount_percentage = 15

    elif order_amount >= 1500:
        discount_percentage = 10

    elif order_amount >= 1000:
        discount_percentage = 7

    else:
        discount_percentage = 0

    # Calculate discount and final amount
    discount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount

    # Add final amount to revenue
    total_revenue = total_revenue + final_amount

    # Count discounted orders
    if discount_percentage > 0:
        discounted_orders = discounted_orders + 1

    # Display order summary
    print(order_amount, "|", discount_percentage, "% |", final_amount)

# Display total revenue
print("----------------------------------------")
print("Total Revenue After Discounts:", total_revenue)

# Extra: Number of discounted orders
print("Number of Discounted Orders:", discounted_orders)
