def F(N):
    i = 1
    x = 1
    C = N - 4
    while C >= x:
        if N > x:
            x = i**2
            i += 1
            print(x)
        else:
            break
F(N = int(input()))
