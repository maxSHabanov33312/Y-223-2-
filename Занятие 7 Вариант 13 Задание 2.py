def F(x):  
    a = []
    for i in range(8):
        print("Введите", i, "элемент")
        a.append(int(input()))
    print(a)
    for i in range(8):
        if a[i] < 15:
            a[i] = a[i]*2
    print(a)
F(x = int(input("Для старта нажмите любое число:" )))
