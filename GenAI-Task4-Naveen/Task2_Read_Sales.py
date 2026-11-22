
# Task 2: Read File in Different Ways

# 1. Read the entire file using read()
with open("sales_data.txt", "r") as file:
    content = file.read()

print("Entire file content:")
print(content)


# 2. Read the first line using readline()
with open("sales_data.txt", "r") as file:
    first_line = file.readline()

print("First line:")
print(first_line.strip())


# 3. Read all lines using readlines()
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# Convert strings into integers
sales_values = [int(line.strip()) for line in lines if line.strip()]

print("Sales values as integers:")
print(sales_values)
