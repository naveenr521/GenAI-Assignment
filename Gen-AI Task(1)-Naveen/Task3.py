
# Task 3: Product Pricing (Dictionaries)

# 1. Create a dictionary with at least 6 products
price_dict = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Monitor": 12000,
    "Headphones": 2000
}

print("Original product prices:")
print(price_dict)

# 2. Add a new product
price_dict["Tablet"] = 15000

print("\nAfter adding a product:")
print(price_dict)

# Update the price of an existing product
price_dict["Laptop"] = 55000

print("\nAfter updating Laptop price:")
print(price_dict)

# Remove a product safely
product_to_remove = "Mouse"

if product_to_remove in price_dict:
    price_dict.pop(product_to_remove)
    print("\nProduct removed successfully.")
else:
    print("\nProduct does not exist.")

# Demonstrate handling a missing product
product_to_remove = "Camera"

if product_to_remove in price_dict:
    price_dict.pop(product_to_remove)
    print("Product removed successfully.")
else:
    print("Camera does not exist.")

# 3. Calculate average price
total_price = sum(price_dict.values())
number_of_products = len(price_dict)

average_price = total_price / number_of_products

print("\nTotal price:", total_price)
print("Number of products:", number_of_products)
print("Average price:", average_price)

# 4. Extra: Find maximum and minimum prices
maximum_price = max(price_dict.values())
minimum_price = min(price_dict.values())

print("\nMaximum price:", maximum_price)
print("Minimum price:", minimum_price)

# Display products with maximum and minimum prices
for product, price in price_dict.items():
    if price == maximum_price:
        print("Highest priced product:", product)

    if price == minimum_price:
        print("Lowest priced product:", product)
