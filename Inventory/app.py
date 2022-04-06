from utils import database, admin_database
import datetime

user_choice = """
- press 'a' to add product ,
- press 's' to sell product ,
- press 'm' to sell more than one product ,
- press 'd' to to see product stock in hand now, 
- press 'r' to re-stock products,
- press 'c' to access admin panel,
- press 'q' to quit the inventory.

Your Choice: """

admin_choice = """
( ADMIN PANEL )
- press 'p' to update any product price,
- press 're' to remove all products,
- press 'rs' to remove a specific product, 
- press 'n' to create a new admin account,
- press 'q' to quit admin panel.

Admin Choice : """


def menu():
    database.create_table()
    admin_database.admin_create_table()
    user_1st = input(user_choice).lower()
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
            prompt_remove_all()

        elif user_1st == "r":
            update()

        elif user_1st == "rs":
            prompt_remove_specific()

        elif user_1st == "c":
            admin_panel()

        else:
            print("Unknown Command.... Please try again.....")

        user_1st = input(user_choice).lower()


def prompt_add():
    try:
        product_code = int(input("Enter a product code of the product: "))
        product_name = input("Enter the name of the product: ").capitalize()
        price = int(input("Enter per unit price: "))
        amount = int(input("Enter the amount of the adding product: "))

        database.add_new_product(product_code, product_name, price, amount, datetime.datetime.now().strftime("%c"))

    except IndexError and ValueError:
        print("Something went wrong. Please try again....")


def prompt_sell():
    try:

        product_code = int(input("Enter a product code of the product: "))
        amount = int(input("Enter the amount of the selling product: "))

        database.sell(product_code, amount, datetime.datetime.now().strftime("%c"))

    except IndexError and ValueError:
        print("Unknown Command.... Please try again with correct product code and amount...")


def more_sell():
    try:
        amount = int(input("Enter how many products you want to sell: "))
        for i in range(amount):
            product_code = int(input("\nEnter a product code of the product: "))
            amount = int(input("Enter the amount of the selling product: "))

            database.sell(product_code, amount, datetime.datetime.now().strftime("%c"))

    except IndexError and ValueError:
        print("Something went wrong.... Please try again with correct number of products.")


def show_all():
    products = database.product_all()
    for product in products:
        print(f"product code: {product['code']}  product name: {product['name']} "
              f"Available: {product['stock now']} Dispatched: {product['dispatched']}"
              f"  Recent sold: {product['sell time']} ")


def prompt_price_update():
    try:

        product_code = int(input("Enter product code to update the price: "))
        price = int(input("Enter the price to update: "))

        database.update_price(product_code, price)

    except IndexError and ValueError:
        print("Something went wrong.... Please try again with correct number")


def update():
    try:
        product_code = int(input("Enter the product code which you want to re-stock: "))
        amount = int(input("Enter how many products to re-stock: "))
        database.re_stock(product_code, amount, datetime.datetime.now().strftime("%c"))

    except IndexError and ValueError:
        print("Unknown Command.... Please try again with correct product code and amount...")


def prompt_remove_specific():
    try:
        product_code = int(input("Enter the product code which you want to remove: "))
        database.remove_specific(product_code)

    except IndexError and ValueError:
        print("something went wrong...Please enter the correct product code..... ")


def prompt_remove_all():
    ask = input("[ALERT!!!!] Do you really want to remove all the products? (Y/n): ").lower()
    if ask == "y":
        database.remove()
        print("NOTICE: You have removed all products...")
    else:
        print("NOTICE: All products exists.. No action occurred..")


def admin_panel():
    all_admin = admin_database.admin_data()

    if all_admin:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")

        for admin in all_admin:
            if admin["username"] == user_name and admin["password"] == password:
                admin_input = input(admin_choice).lower()
                while admin_input != "q":
                    if admin_input == "p":
                        prompt_price_update()

                    elif admin_input == "re":
                        prompt_remove_all()

                    elif admin_input == "rs":
                        prompt_remove_specific()

                    elif admin_input == "n":
                        create_admin_account()

                    else:
                        print("Unknown Command... Please try again.")

                    admin_input = input(admin_choice)



    elif not all_admin:
            print("NO admin account found... please login with the default account...")
            admin_database.add_admin_data(admin_database.default_user(), admin_database.default_user(), "admin@gmail.com")


def create_admin_account():
    user_name = input("Enter the username: ")
    email = input("Enter your email address: ")
    password = input("Enter the password: ")
    confirm_pass = input("Confirm your password: ")

    if password == confirm_pass:
        admin_database.add_admin_data(user_name, confirm_pass, email)

    else:
        print("password not matched...")


menu()
