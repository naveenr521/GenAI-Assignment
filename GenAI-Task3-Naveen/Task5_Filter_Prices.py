
# Task 5: Using filter() - Filter Expensive Products

prices = [100, 250, 400, 1200, 50, 2000, 850]

# Filter prices greater than 500
expensive_prices = list(filter(lambda price: price > 500, prices))

# Filter prices less than or equal to 500
affordable_prices = list(filter(lambda price: price <= 500, prices))

# Display the results
print("Expensive prices:", expensive_prices)
print("Affordable prices:", affordable_prices)
