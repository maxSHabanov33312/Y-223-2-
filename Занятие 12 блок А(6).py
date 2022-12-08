def f(n, s):
    x  = 0
    if n <= 1:
        x = print("Некоректное число")
    else:
        if n == 2:  
            x = print("YES")
        else:
            if n <= 1 or n % 2 == 0:
                x = print("NO")
            else:
                if s * s > n:
                    x = print("YES")
                else:
                    if (n % s) == 0:  
                        x = print("NO")
                    else:  
                        x = f(n, s+2)
    return x
f(n = int(input("Введите число больше 1: ")), s = 3)
