from utils import database

user_choice = """
- press 'a' to add product ,
- press 's' to sell product , 
- press 'd' to to see product stock in hand now, 
- press 'q' to quit the inventory.
"""

def menu():
    database.create_table()
    user_1st = input(user_choice)
    while user_1st != "q":
        if user_1st == "a":
            prompt_add()
        elif user_1st == 's':
            prompt_sell()
        elif user_1st == 'd':
            pass

        else:
            print("Unknown Command.... Please try again.....")

        user_1st = input(user_choice)


def prompt_add():
    product_code= input("Enter a product code of the product: ")
    product_name = input("Enter the name of the product: ")
    pack_size = input("Enter pack size of the product: ")
    Rate = input("Enter per unit price: ")
    amount = int(input("Enter the amount of the adding product: "))


    database.add_new_product(product_code,product_name,pack_size,Rate,amount)

def prompt_sell():
    product_code= input("Enter a product code of the product: ")
    amount = int(input("Enter the amount of the adding product: "))

    database.sell(product_code,amount)












menu()



