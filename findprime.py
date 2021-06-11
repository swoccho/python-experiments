for n in range(2,20):
    for i in range(2,n):
        if n % i ==0:
            print(f'{n} equals {i} * {n//i}')
            break
    else:
        print(f"{n} is a prime number")
        