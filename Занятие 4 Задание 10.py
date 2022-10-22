def Fubonacchi(N,K): #Нуждается в доработке
    X = 0
    Z = 0
    D = X
    list = []
    a = 1
    y = 0
    for i in range(1, N):
        b = a
        a = b + y
        y = b
        list.append(b)
    list.insert(0, 0)
    print(list)
    for i in list:
        while K < N:
            Z = list[K]
            X += Z
            K = K+i
    print(X)
Fubonacchi(N = int(input()), K = int(input()))
