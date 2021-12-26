from utils import database

user_choice = """
- press 'a' to add product ,
- press 's' to sell product ,
- press 'm' to sell more than one product ,
- press 'd' to to see product stock in hand now, 
- press 'r' to re-stock products,
- press 'q' to quit the inventory.

Your Choice: """


def menu():
    database.create_table()
    user_1st = input(user_choice)
    while user_1st != "q":
        if user_1st == "a":
            prompt_add()
        elif user_1st == 's':
            prompt_sell()

        elif user_1st == "m":
            more_sell()
        elif user_1st == 'd':
            show_all()
        elif user_1st == "re":
            database.remove()

        elif user_1st == "u":
            prompt_price_update()

        elif user_1st == "r":
            update()

        elif user_1st == "rs":
            try:
                product_code = int(input("Enter the product code which you want to remove: "))
                database.remove_specific(product_code)

            except IndexError and ValueError:
                print("something went wrong...Please enter the correct product code..... ")

        else:
            print("Unknown Command.... Please try again.....")

        user_1st = input(user_choice)


def prompt_add():
    try:
        product_code = int(input("Enter a product code of the product: "))
        product_name = input("Enter the name of the product: ")
        price = int(input("Enter per unit price: "))
        amount = int(input("Enter the amount of the adding product: "))

        database.add_new_product(product_code, product_name, price, amount)

    except IndexError and ValueError:
        print("Something went wrong. Please try again....")


def prompt_sell():
    try:

        product_code = int(input("Enter a product code of the product: "))
        amount = int(input("Enter the amount of the selling product: "))

        database.sell(product_code, amount)

    except IndexError and ValueError:
        print("Unknown Command.... Please try again with correct product code and amount...")


def more_sell():
    try:
        amount = int(input("Enter how many products you want to sell: "))
        for i in range(amount):
            product_code = int(input("\nEnter a product code of the product: "))
            amount = int(input("Enter the amount of the selling product: "))

            database.sell(product_code, amount)

    except:
        print("Something went wrong.... Please try again with correct number of products.")


def show_all():
    products = database.product_all()
    for product in products:
        print(f"product code: {product['code']}  product name: {product['name']} "
              f"Available: {product['stock now']} Dispatched: {product['dispatched']} ")


def prompt_price_update():
    product_code = int(input("Enter product code to update the price: "))
    price = int(input("Enter the price to update: "))

    database.update_price(product_code, price)


def update():
    try:
        product_code = int(input("Enter the product code which you want to re-stock: "))
        amount = int(input("Enter how many products to re-stock: "))
        database.re_stock(product_code, amount)

    except IndexError and ValueError:
        print("Unknown Command.... Please try again with correct product code and amount...")


menu()
