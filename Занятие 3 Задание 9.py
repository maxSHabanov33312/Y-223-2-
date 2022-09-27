def add(n,m,k):
    s = n*m
    if s > k and ((k%n == 0) or (k % m == 0)):
        print("Да")
    else:
        print("Нет")
add(n = int(input()), m = int(input()), k = int(input()))
