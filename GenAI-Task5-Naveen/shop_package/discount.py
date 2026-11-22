
# Apply percentage discount
def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount


# Apply flat discount of Rs. 50
def flat_discount(price):
    return price - 50
