
# Task 4: Using map() - Apply GST to List of Prices

prices = [100, 250, 400, 1200, 50]

# Lambda function to calculate GST
gst = lambda price: price + (0.18 * price)

# Apply GST to all prices using map()
prices_with_gst = list(map(gst, prices))

# Display the results
print("Original prices:", prices)
print("Prices after GST:", prices_with_gst)
