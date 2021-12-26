import sqlite3


def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS inventory(product_code integer primary key ,"
                   "product_name text , price integer , Last_stock integer ,"
                   " Stock_in_hand integer,Dispatched_stock integer,Total_earning integer)")

    connection.commit()
    connection.close()


def add_new_product(product_code, product_name, price, amount):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    dispatched = 0
    total_earning = 0
    try:
        cursor.execute("INSERT INTO inventory VALUES(?,?,?,?,?,?,?)", (product_code, product_name,
                                                                       price, amount, amount,
                                                                       dispatched, total_earning,))
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
        {"code": row[0], "name": row[1], "price": row[2], "last stock": row[3], "stock now": row[4],
         "dispatched": row[5], "total earning": row[6]} for row in cursor.fetchall()]

    connection.close()
    return products


def sell(product_code, amount):
    all_product = product_all()

    connection = sqlite3.connect("data.db")

    cursor = connection.cursor()
    try:

        stock = [product["stock now"] for product in all_product if product["code"] == product_code]
        dispatched = [product["dispatched"] for product in all_product if product["code"] == product_code]
        total_earning = [product["total earning"] for product in all_product if product["code"] == product_code]
        price = [product["price"] for product in all_product if product["code"] == product_code]
        s = stock[0]
        stock_now = stock[0] - amount
        dispatched_total = dispatched[0] + amount
        total_earning_now = price[0] * amount + total_earning[0]

        if stock_now > 0:
            if stock_now < 20:
                print(f"\nThe product code {product_code} is remaining {stock_now}.. Please re_stock the product.")
            cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=? ", (stock_now, product_code,))
            cursor.execute("UPDATE inventory SET Dispatched_stock=? WHERE product_code=? ",
                           (dispatched_total, product_code,))
            cursor.execute("UPDATE inventory SET Total_earning=? WHERE product_code=?",
                           (total_earning_now, product_code,))

            connection.commit()
            connection.close()
        else:
            print(f"product code {product_code} is not available {amount} piece. Available amount: {s} ")

    except:
        print(f"\nProduct code {product_code} is not available")


def update_price(product_code, price):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE inventory SET price=? WHERE product_code=? ", (price, product_code))
    connection.commit()
    connection.close()


def re_stock(product_code, amount):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    all_products = product_all()
    try:
        stock = [product["stock now"] for product in all_products if product_code == product["code"]]
        stock_now = stock[0] + amount
        cursor.execute("UPDATE inventory SET Stock_in_hand=? WHERE product_code=?", (stock_now, product_code,))
        cursor.execute("UPDATE inventory SET Last_stock=? WHERE product_code=?", (amount, product_code,))
        connection.commit()
        connection.close()

    except IndexError:
        print(f"\nProduct code {product_code} is not available")




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
