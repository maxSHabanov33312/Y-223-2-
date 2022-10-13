def Fubonacchi(Z, K, N): #Нуждается в доработке
    X = 0
    list = []
    a = 1
    y = 0
    for i in range(1, Z):
        b = a
        a = b + y
        y = b
        list.append(b)
    list.insert(0, 0)
    print(list)
    repeat = N - K
    for i in range(repeat + 1):
        znach = list[K + i]
        X += znach
    print(X)
Fubonacchi(Z = int(input()), K = int(input()), N = int(input()))
