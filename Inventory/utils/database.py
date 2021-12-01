from .database_connection import DatabaseConnection

def create_table():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS inventory(product_code integer primary key ,"
                       "product_name text ,pack_size text ,Rate integer ,Last_stock integer,"
                       " Stock_in_hand integer,Dispatched_stock integer)")




def add_new_product(product_code,product_name,pack_size,Rate,amount):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        dispatced = 0
        cursor.execute("INSERT INTO inventory VALUES(?,?,?,?,?,?,?)" ,(product_code,product_name,pack_size,Rate,amount,amount,dispatced,))



def product_all():
    with DatabaseConnection("data.db") as connection :
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM inventory")

        products = [{"code":row[0] , "name" : row[1], "pack size" : row[2], "rate": row[3] , "last stock" : row[4] , "stock now" : row[5] , "dispatched" : row[6]} for row in cursor.fetchall()]
        return  products


# stock = [product["stock now"] for product in product_all()]
# dispatced = [product["dispatched"] for product in product_all()]
def sell(product_code, amount):
    # global stock , dispatced

    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        all = product_all()
        # for product in range(len(all)):
        #     if all[product]["code"] == product_code:
        #         for product in all:
        #             stock = product["stock now"] - amount
        #             dispatced = product["dispatched"] +amount



        for product in all:


                #
                # stock = int(s)
                # dispatced = int(d)
                # stock -= amount
                # dispatced += amount



            stock = product["stock now"]
            dispatced =product["dispatched"]
            # while product["code"] == product_code:

        # stock= int(s)
        # dispatced = int(d)
    #
            stock -= amount
            dispatced += amount

        cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=? ",(stock, product_code,))
        cursor.execute("UPDATE inventory SET Dispatched_stock=? WHERE product_code=? " , (dispatced,product_code,))




# def re_stock(product_code,re_amount):
#     with DatabaseConnection("data.db") as connection:
#         cursor = connection.cursor()
#         all = product_all()
#         for product in all:
#             s = product["stock now"]
#             stock = int(s)
#
#             stock =stock+re_amount
#
#         cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=?", (stock,product_code,))




