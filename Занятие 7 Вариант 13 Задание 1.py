def F(n):
    a = []
    b = []
    c = []
    for i in range(n):
        print("Введите", i, "элемент")
        a.append(int(input()))
    print(a)
    for i, x in enumerate(a):
        if x in a[:i]:
            b.append(x)
            c.append(i)
    print(b)
    print(c)
F(n = int(input("Введите длину массива ")))
