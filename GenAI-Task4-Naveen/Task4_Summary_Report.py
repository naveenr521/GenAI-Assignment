
# Task 4: Generate Sales Summary

# Read sales data from the file
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# Convert the values into integers
sales = [int(line.strip()) for line in lines if line.strip()]

# Calculate sales details
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# Display the summary
print("Sales Summary Report")
print("--------------------")
print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)
