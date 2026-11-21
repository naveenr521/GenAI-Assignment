
# Task 3: User Menu (while loop + break/continue)

# Create an empty list to store orders
orders = []

while True:

    print("\n========== ORDER MENU ==========")
    print("1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")
    print("================================")

    choice = input("Enter your choice: ").lower()

    # Quit option
    if choice == "q":
        print("Exiting the program. Thank you!")
        break

    # Add order option
    elif choice == "1":

        try:
            order_amount = int(input("Enter order amount: "))

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        orders.append(order_amount)

        print("Order added successfully!")

    # Show all orders option
    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total_revenue = 0

        print("\nOrder Amount | Discount | Final Amount")
        print("----------------------------------------")

        for order_amount in orders:

            if order_amount >= 2000:
                discount_percentage = 15

            elif order_amount >= 1500:
                discount_percentage = 10

            elif order_amount >= 1000:
                discount_percentage = 7

            else:
                discount_percentage = 0

            discount = order_amount * discount_percentage / 100

            final_amount = order_amount - discount

            total_revenue = total_revenue + final_amount

            print(order_amount, "|", discount_percentage,
                  "% |", final_amount)

        print("----------------------------------------")
        print("Total Revenue:", total_revenue)

    # Invalid menu choice
    else:
        print("Invalid choice. Please select 1, 2 or q.")
        continue
