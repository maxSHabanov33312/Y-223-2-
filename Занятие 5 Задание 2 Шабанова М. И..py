def F(n):
    i = 2
    if n > 2: 
        while n%i != 0:
            i += 1
        print(i)
    else:
        print("Неверное число!")
F(n = int(input()))
