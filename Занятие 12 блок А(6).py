def f(n, s=3):
    if n == 2:  
        x = print("YES")
    elif n <= 1 or n % 2 == 0:  
        x = print("NO")
    elif s * s > n:  
        x = print("YES")
    elif (n % s) == 0:  
        x = print("NO")
    else:  
        x = f(n, s+2)
    return x
f(n = int(input("Введите число больше 1: ")), s = 2)
