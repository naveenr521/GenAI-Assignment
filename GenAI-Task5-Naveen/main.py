# ==========================================
# TASK 1: IMPORTING MATH MODULE
# ==========================================

import math_utils
from math_utils import square

print("\n--- MATH MODULE ---")

print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(5))


# ==========================================
# TASK 2: IMPORTING STRING MODULE
# ==========================================

import string_utils

print("\n--- STRING MODULE ---")

text = "hello python programming"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# ==========================================
# TASK 4: IMPORTING SHOP PACKAGE
# ==========================================

import shop_package.discount as disc

from shop_package.billing import calculate_total, apply_tax

print("\n--- SHOP PACKAGE ---")

# Percentage discount
print("Percentage Discount:", disc.apply_discount(1000, 10))

# Flat discount
print("Flat Discount:", disc.flat_discount(1000))

# Calculate total bill
print("Total Bill:", calculate_total([100, 200, 300]))

# Apply tax
print("Bill with Tax:", apply_tax(1000))