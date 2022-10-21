def F(N,n):
    sum = n
    for i in range(N-1):
        n = int(input())
        sum += n
    print(N)
    print(sum)     
F(N = int(input()),n = int(input()))
