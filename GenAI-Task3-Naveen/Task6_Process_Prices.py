
# Task 6: Combined Utility Function

def process_prices(prices):

    # Apply 10% discount using map()
    discounted_prices = list(
        map(lambda price: price - (price * 10 / 100), prices)
    )

    # Keep discounted prices greater than 300
    filtered_prices = list(
        filter(lambda price: price > 300, discounted_prices)
    )

    # Return both lists
    return discounted_prices, filtered_prices


# Test the function
discounted_prices, filtered_prices = process_prices([100, 500, 900, 50, 750])

print("Discounted prices:", discounted_prices)
print("Filtered prices:", filtered_prices)
