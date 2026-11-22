
# Task 1: Basic Function - Price After Discount

def apply_discount(price, discount_percent=5):
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return final_price


# Test the function
result1 = apply_discount(1000, 10)
result2 = apply_discount(500)

print("Price after 10% discount:", result1)
print("Price after default 5% discount:", result2)
