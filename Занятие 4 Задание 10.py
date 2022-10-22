def F(N,K):
    X = 0
    Z = 0
    K = K - 1
    list = []
    a = 1
    y = 0
    for i in range(1, N):
        b = a
        a = b + y
        y = b
        list.append(b)
    list.insert(0, 0)
    for i in list:
        while K < N:
            Z = list[K]
            X += Z
            K = K+1
    print(X)
F(N = int(input()), K = int(input()))
