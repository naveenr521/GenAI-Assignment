
# Task 7: Mini Project - Export Discounted Prices

# Product price dictionary
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Get discount percentage from user
discount_percent = float(input("Enter discount percentage: "))

# Open report file in write mode
with open("discount_report.txt", "w") as file:

    file.write("Product | Original Price | Discounted Price\n")
    file.write("-------------------------------------------\n")

    discounted_prices = []

    # Calculate discounted prices
    for product, price in prices.items():

        discount_amount = price * discount_percent / 100
        discounted_price = price - discount_amount

        discounted_prices.append(discounted_price)

        file.write(
            f"{product} | {price:.2f} | {discounted_price:.2f}\n"
        )

    # Optional summary
    total_items = len(discounted_prices)
    average_discounted_price = sum(discounted_prices) / total_items

    file.write("\nSummary\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(
        f"Average Discounted Price: {average_discounted_price:.2f}\n"
    )


# Read and display the report
with open("discount_report.txt", "r") as file:
    report = file.read()

print("\nDiscount Report:")
print(report)
