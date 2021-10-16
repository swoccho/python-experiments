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



def sell(product_code, amount):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        all = product_all()
        for product in all:
            s = product["stock now"]
            d = product["dispatched"]
        stock= int(s)
        dispatced = int(d)

        stock -= amount
        dispatced += amount

        cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=? ",(stock, product_code,))
        cursor.execute("UPDATE inventory SET Dispatched_stock=? WHERE product_code=? " , (dispatced,product_code,))




