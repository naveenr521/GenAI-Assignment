
# Task 1: Product Collections (Lists and Tuples)

# 1. Create a list containing at least 6 products
products = [
    "Laptop",
    "Mobile",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones"
]

# 2. Create a tuple for one product
sample_product = ("Laptop", 50000, "Electronics")

# 3. Print the second and last product
print("Second product:", products[1])
print("Last product:", products[-1])

# 4. Append two new products
products.append("Tablet")
products.append("Speaker")

# Print the updated list
print("Updated product list:", products)

# 5. Extra: Convert tuple into a list
sample_product_list = list(sample_product)

# Change the price
sample_product_list[1] = 55000

# Convert list back into tuple
sample_product = tuple(sample_product_list)

print("Updated sample product:", sample_product)
