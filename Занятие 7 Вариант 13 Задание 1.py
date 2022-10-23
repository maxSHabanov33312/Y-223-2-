def F(n):   
    a = []
    b = []
    for i in range(n):
        print("Введите", i, "элемент")
        a.append(int(input()))
    print(a)
    for i in a:
        if a.count(i) > 1:
            b.append(i)
    c = a.index(a[i], a.count(i) > 1) 
    print(b)
    print(c)
F(n = int(input("Введите длину массива ")))
