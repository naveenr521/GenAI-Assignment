
# Task 4: Combined Operations

# 1. Create the products list
products = [
    "Laptop",
    "Mobile",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones"
]

# Create the price dictionary
price_dict = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Monitor": 12000,
    "Headphones": 2000
}

# Create a parallel categories list
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Accessories"
]

# 2. Create a list of tuples named catalog
catalog = []

for i in range(len(products)):
    product_name = products[i]
    price = price_dict[product_name]
    category = categories[i]

    catalog.append((product_name, price, category))

print("Product catalog:")
for item in catalog:
    print(item)

# 3. Create category_to_products dictionary
category_to_products = {}

for item in catalog:
    product_name = item[0]
    category = item[2]

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product_name)

print("\nCategory wise products:")
print(category_to_products)

# 4. Find the category with the maximum number of products
maximum_category = ""
maximum_count = 0

for category in category_to_products:
    product_count = len(category_to_products[category])

    if product_count > maximum_count:
        maximum_count = product_count
        maximum_category = category

print("\nCategory with maximum products:", maximum_category)
print("Number of products:", maximum_count)

# Print all products belonging to that category
print("Products in that category:")

for product in category_to_products[maximum_category]:
    print(product)
