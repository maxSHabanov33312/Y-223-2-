N = int(input("Введите длину ряда: ")) #Требуется доработка
K = int(input())
f1 = f2 = 1
for i in list(range(2, N)):
    f1, f2 = f2, f1 + f2
    print(f1, f2, end=" ")
    x = K in list(range(2, N))
    y = N in list(range(2, N))
    print(sum(range(x, y)))
