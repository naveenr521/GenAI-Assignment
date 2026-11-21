
# Task 5: Loop Control with Conditions

# Given daily sales
daily = [200, 150, 0, 400, 50, -1, 300]

# Initialize total sales
total_sales = 0

# Iterate through daily sales
for sale in daily:

    # Check for corrupted data
    if sale == -1:
        print("Corrupted data detected. Stopping processing.")
        break

    # Skip days with zero sales
    elif sale == 0:
        print("No sales today. Skipping.")
        continue

    # Add valid positive sales
    else:
        total_sales = total_sales + sale

        print("Daily Sales:", sale)
        print("Running Total:", total_sales)

# Print final total
print("\nFinal Total Sales:", total_sales)

