
# Task 2: Categories (Sets)

# Create a products list
products = [
    "Laptop",
    "Mobile",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones"
]

# Create a parallel categories list
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Accessories"
]

# 1. Create a set of categories
categories_set = set(categories)

print("Original categories:", categories_set)

# 2. Add a new category
categories_set.add("Furniture")

print("After adding a category:", categories_set)

# Demonstrate duplicate handling
categories_set.add("Electronics")

print("After adding duplicate:", categories_set)

# 3. Check whether a category exists
print("Is Electronics available?",
      "Electronics" in categories_set)

print("Is Clothing available?",
      "Clothing" in categories_set)

# 4. Extra: Count unique categories
print("Total unique categories:", len(categories_set))
