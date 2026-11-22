
# Task 7: Mini Problem - Menu Using Functions

# Function to add a price
def add_price(prices_list, price):
    prices_list.append(price)
    print("Price added successfully.")


# Function to calculate average price
def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0

    return sum(prices_list) / len(prices_list)


# Function to get maximum price
def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0

    return max(prices_list)


# Main program
prices = []

while True:

    print("\n----- PRICE MENU -----")
    print("1. Add price")
    print("2. Show average price")
    print("3. Show highest price")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":

        price = float(input("Enter the price: "))
        add_price(prices, price)

    elif choice == "2":

        average = get_average_price(prices)
        print("Average price:", average)

    elif choice == "3":

        highest = get_max_price(prices)
        print("Highest price:", highest)

    elif choice.lower() == "q":

        print("Exiting the program.")
        break

    else:

        print("Invalid choice. Please try again.")
