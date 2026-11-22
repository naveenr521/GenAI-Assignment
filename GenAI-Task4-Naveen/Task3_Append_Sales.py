
# Task 3: Append New Sales

new_sales = [5000, 2500, 1700]

# Open the file in append mode
with open("sales_data.txt", "a") as file:

    for sale in new_sales:
        file.write(str(sale) + "\n")

# Read the updated file
with open("sales_data.txt", "r") as file:
    updated_content = file.read()

print("Updated sales records:")
print(updated_content)
