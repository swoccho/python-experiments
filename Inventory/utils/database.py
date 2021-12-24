import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS inventory(product_code integer primary key ,"
                   "product_name text , Rate integer , Last_stock integer ,"
                   " Stock_in_hand integer,Dispatched_stock integer)")

    connection.commit()
    connection.close()


def add_new_product(product_code, product_name, rate, amount):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    dispatched = 0
    try:
        cursor.execute("INSERT INTO inventory VALUES(?,?,?,?,?,?)", (product_code, product_name,
                                                                     rate, amount, amount, dispatched,))
    except sqlite3.IntegrityError:
        print(F"\nThe product of code  {product_code} is already exist.\nTo Update the product price press 'v' or to "
              F"re-stock the product press 'n' ")
    connection.commit()
    connection.close()


def product_all():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inventory")

    products = [
        {"code": row[0], "name": row[1], "rate": row[2], "last stock": row[3], "stock now": row[4],
         "dispatched": row[5]} for row in cursor.fetchall()]

    connection.close()
    return products


def sell(product_code, amount):
    all_product = product_all()

    connection = sqlite3.connect("data.db")

    cursor = connection.cursor()
    try:

        stock = [product["stock now"] for product in all_product if product["code"] == product_code]
        dispatched = [product["dispatched"] for product in all_product if product["code"] == product_code]
        s = stock[0]
        stock_now = stock[0] - amount
        dispatched_total = dispatched[0] + amount
        if stock_now > 0:
            if stock_now < 20:
                print(f"\nThe product code {product_code} is remaining {stock_now}.. Please re_stock the product.")
            cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=? ", (stock_now, product_code,))
            cursor.execute("UPDATE inventory SET Dispatched_stock=? WHERE product_code=? ",
                           (dispatched_total, product_code,))

            connection.commit()
            connection.close()
        else:
            print(f"product code {product_code} is not available {amount} piece. Available amount: {s} ")

    except:
        print(f"\nProduct code {product_code} is not available")


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
    cursor.execute("DELETE FROM inventory WHERE product_code =?", (product_code,))
    connection.commit()
    connection.close()
