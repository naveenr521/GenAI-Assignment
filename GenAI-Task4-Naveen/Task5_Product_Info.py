
# Task 5: Create Product Info File

# Open the file in write mode
with open("products.txt", "w") as file:

    # Get details of three products
    for i in range(3):
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))

        # Write product details into the file
        file.write(f"{product_name} | {product_price:.2f}\n")


# Read and display the product information
with open("products.txt", "r") as file:
    print("\nProduct Information:")
    print("--------------------")

    for line in file:
        print(line.strip())
