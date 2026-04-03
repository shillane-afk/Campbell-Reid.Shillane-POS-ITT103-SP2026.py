# ------------------ POINT OF SALE SYSTEM ------------------



# PRODUCT LIST WITH TEN ITEMS
# The variable called "products" stores MANY items inside ONE variable.
# It is a LIST, meaning it can hold multiple things in order.
# Each product inside is ALSO a LIST.
# I used list so that the stock can later be changed.

# Each small box has 4 things:
# [0] = product code
# [1] = product name
# [2] = product price
# [3] = stock quantity
products = [
    ["GRO001", "Bread", 450, 25],
    ["GRO002", "Rice", 800, 40],
    ["GRO003", "Pasta", 300, 30],
    ["GRO004", "Eggs", 700, 50],
    ["GRO005", "Milk", 600, 35],
    ["GRO006", "Cooking oil", 1200, 20],
    ["GRO007", "Sugar", 500, 45],
    ["GRO008", "Salt", 150, 60],
    ["GRO009", "Flour", 550, 25],
    ["GRO010", "Chicken", 1500, 15]
]



# CART
# This starts as an EMPTY list.
# As user adds items, we will put items INTO this list. No item will be replaced, only added once its in stock.
# Each item added will look like: [code, name, price, quantity].
cart = []



# THIS FUNCTION DISPLAYS THE PRODUCTS ON THE SCREEN AT THE BEGINNING OF THE PROGRAM.
def display_products():

    print("\nPRODUCT LIST")

    # "product", the temporary variable (represents ONE product at a time).
    # This loop goes through EACH product one by one.
    # Python takes the first product, then second, etc.

    for product in products:

        # product is one list.
        # This is an example of what each represent: ["GRO001", "Bread", 450, 25].

        # I assigned each variable to each part using POSITION (index).

        code = product[0]     # first item (position 0)
        name = product[1]     # second item (position 1)
        price = product[2]    # third item (position 2)
        stock = product[3]    # fourth item (position 3)

        # Print all values
        print(code, "-", name, ", Price:", price, ", Stock:", stock)

        # This will print a low stock alert if the stock quantity if 4 or less.
        if stock < 5:
            print("LOW STOCK")



# THIS FUNCTION ADDS ITEMS TO CART
def add_to_cart():

    try:
        # This prompts the user to enter a product code.
        code = input("Enter product code: ").upper()

        # This function loops through products to find the correct one.
        for product in products:

            # Compare user input with product code.
            if code == product[0]:

                # This prompts the user to input quantity of product.
                quantity = int(input("Enter quantity: "))

                # This prevents invalid quantity input.
                if quantity <= 0:
                    print("Quantity must be greater than 0")

                    # Return ends the loop.
                    return

                # This block test for stock availability before anything is added to cart.
                # The quantity must be equal or less than products to be added to cart.
                # Otherwise, if products and quantity ia at 0, it will print "Not enough stock".
                # This block of code and the one directly above, creates a perfectly controlled environment.
                if quantity > product[3]:
                    print("Not enough stock")
                    return

                # This checks if an item was already added to the cart. The default is false until a product is added.
                found = False

                for item in cart:

                    # This checks if item already exists in the cart in order to carry out the function below. This avoids duplicates.
                    if item[0] == code:

                        # This increase quantity by increments to the value instead of adding new items.
                        # old quantity + new quantity
                        item[3] += quantity

                        # This checks whether the temporary variable "item," representing the positional index during iteration, is equivalent to the user-provided "code".
                        # Therefore, found = True if it is true as seen above "item[0] == code:"
                        found = True

                # If item was NOT found in cart.
                if not found:

                    # This allows the user to add new items into the cart.
                    # The variable "cart = []" which is blank, "append" simply allows for the cart to be updated.
                    # If the already exists, it will update it.
                    # If the item does not exist, it will add it as new.
                    cart.append([product[0], product[1], product[2], quantity])

                # The reason why this block of code is indented to this level is because, it responds to two things;
                # It responds to when a new item is added, "if not found:", hence, cart.append([product[0], product[1], product[2], quantity]).
                # and when an item is added by increments, if item[0] == code:, hence, "item[3] += quantity".
                print("Item added to cart")
                return

        # If no match found
        print("Invalid product code")

    except ValueError:
        # If user enters wrong data (like letters instead of number). This allows an output instead of the program crashing.
        print("Invalid input")



# REMOVE ITEM/S FROM CART
# This function allows the user to remove an item using the product code.
def remove_from_cart():
    try:
        code = input("Enter product code to remove: ").upper()

        # This function enables allows loop through the cart to find the code that was inputted by the user.
        for item in cart:

            if item[0] == code:

                # This function removes item/s from the cart.
                cart.remove(item)

                print("Item removed")
                return

        print("Item not found in cart")

    except ValueError:
        # If user enters wrong data (like letters instead of number). This allows an output instead of the program crashing.
        print("Invalid input")


# VIEW CART
# This function allows the user to view cart.
def view_cart():

    print("\nCART")

    if len(cart) == 0:
        print("Cart is empty")
        return

    # Declaration of variable that will be used below.
    total = 0

    for item in cart:

        # This allows all the items in the cart to be ordered as per the position index below.
        name = item[1]
        price = item[2]
        quantity = item[3]

        # This formula allows the price to be calculated for each type item by multiplying price by quantity.
        item_total = price * quantity

        # This function allows the subtotal total price to be calculated for each type of item by adding all "item totals".
        total += item_total

        print(name, " Quantity:", quantity, " Total:", item_total)

    print("Subtotal:", total)



# CHECKOUT
# This function is responsible for checking out of items.
def checkout():

    if len(cart) == 0:
        print("Cart is empty")
        return
    # Declaration of variable that will be used below.
    subtotal = 0

    # This function is responsible to calculate subtotal.
    for item in cart:

        # This is the positional index for price * quantity
        subtotal += item[2] * item[3]

    # This is the discount system. Declaration of variable that will be used below.
    discount = 0

    if subtotal > 5000:
        discount = subtotal * 0.05

    subtotal = subtotal - discount

    # This function applies a 10% tax to the subtotal.
    tax = subtotal * 0.10

    total = subtotal + tax

    print("\nSubtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Total:", total)

    try:
        payment = float(input("Enter payment: "))

        # This function validates the payment added by the user.
        if payment < total:
            print("Not enough payment")
            return

        change = payment - total

        # STOCK UPDATE (this is why the list was used)
        for item in cart:

            code = item[0]
            quantity = item[3]

            # This function locates the product in product list at the top.
            for product in products:

                if product[0] == code:

                    # This function reduces the stock. Product in this case represents the amount of product in the list above.
                    # Quantity is the amount of items the customer bought.
                    # When we minus what we have from what was bought, we will be left with a new sum of items.
                    product[3] -= quantity



        # RECEIPT
        print("\nRECEIPT")
        print("Best Buy Retail Store")

        # This function is responsible for printing receipts for good purchased.
        for item in cart:
            print(item[1], " Qty:", item[3], " Price:", item[2])

        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Total:", total)
        print("Paid:", payment)
        print("Change:", change)
        print("Thank you for shopping")

        # This function clears the cart for the next transaction.
        cart.clear()

    except ValueError:
        print("Invalid payment")



# MAIN MENU
# This function allows for a menu-driven system.
def main():

    while True:

        print("\nPoint Of Sale Menu")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            remove_from_cart()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("EXITING")
            break

        else:
            print("Invalid selection")



# START PROGRAM
# This calls the function that was created above.
main()

print("\nI CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT.")