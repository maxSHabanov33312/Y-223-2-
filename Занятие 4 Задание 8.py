def F(n):
    if n<=9:
        for i in range(1,n+1):
            for s in range(1,i+1):
               print(s,end=" ")
            print()
    else:
        print("Неверное значение")
F(n = int(input()))
