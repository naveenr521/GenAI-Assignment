
# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

# Open the file in write mode
with open("sales_data.txt", "w") as file:

    # Write each sale on a separate line
    for sale in sales:
        file.write(str(sale) + "\n")

# Reopen the file and read its contents
with open("sales_data.txt", "r") as file:
    content = file.read()

print("Sales records:")
print(content)
