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
            show_all()

        # elif user_1st == "u":
        #     update()

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
    amount = int(input("Enter the amount of the selling product: "))


    database.sell(product_code,amount)



def show_all():
     products = database.product_all()
     for product in products:
         print(f"product code: {product['code']}  product name: {product['name']} Available: {product['stock now']}")


# def update():
#     global stock
#     product_code = input("Enter a product code of the product: ")
#     re_amount = int(input("Enter the amount of the adding product: "))
#
#     products = database.product_all()
#     for product in products:
#         while product["code"] == product_code:
#             s = product["stock now"]
#             stock_ = int(s)
#             stock = stock_ + re_amount
#
#     database.re_stock(product_code,stock)
#
#
#
#
#








menu()
