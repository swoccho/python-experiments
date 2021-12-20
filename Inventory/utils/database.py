
import sqlite3


def create_table():
    connection= sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS inventory(product_code integer primary key ,"
                       "product_name text ,pack_size text ,Rate integer ,Last_stock integer,"
                       " Stock_in_hand integer,Dispatched_stock integer)")

    connection.commit()
    connection.close()




def add_new_product(product_code,product_name,pack_size,Rate,amount):
    connection = sqlite3. connect("data.db")
    cursor = connection.cursor()
    dispatced = 0
    cursor.execute("INSERT INTO inventory VALUES(?,?,?,?,?,?,?)" ,(product_code,product_name,pack_size,Rate,amount,amount,dispatced,))
    connection.commit()
    connection.close()


def product_all():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inventory")

    products = [{"code":row[0] , "name" : row[1], "pack size" : row[2], "rate": row[3] , "last stock" : row[4] , "stock now" : row[5] , "dispatched" : row[6]} for row in cursor.fetchall()]

    connection.close()
    return  products

def sell(product_code,amount):


    all = product_all()

    connection = sqlite3.connect("data.db")

    cursor = connection.cursor()

    stock = [product["stock now"]  for product in all if product["code"] == product_code ]
    dispached = [product["dispatched"] for product in all if product["code"] == product_code ]

    s = stock[0] - amount
    d = dispached[0] + amount

    cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=? ",(s, product_code,))
    cursor.execute("UPDATE inventory SET Dispatched_stock=? WHERE product_code=? " , (d,product_code,))

    connection.commit()
    connection.close()

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

# def stock():
    

def remove():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory ")
    connection.commit()
    connection.close()

def remove_specific(product_code):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE product_code =?",(product_code,))
    connection.commit()
    connection.close()




