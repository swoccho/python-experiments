cars= ["ok", "ok", "ok", "ok", "problem", "ok", "problem"]

for car in cars :
    if car == "problem":
        print(f"this car have {car}..")
        print("shippning another car to the customer")
        continue
    print(f"this car is {car} ...")
    print("shiping this car to the customers")
else:
    print("All perfect cars have shipped to the customers.... No faulty cars has shipped")