
# Task 6: Read File Safely

import os

filename = input("Enter the filename to open: ")

# Check whether the file exists
if os.path.exists(filename):

    # Open and read the file
    with open(filename, "r") as file:
        content = file.read()

    print("\nFile content:")
    print(content)

else:
    print("File not found. Please check the filename.")
