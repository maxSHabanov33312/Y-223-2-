import random
def f(n):
    s = random.randint(2,n)
    if n > 1:
        if n%1==0 and n%n==0 and n%s==0:
            return f(n) 
        else:
            print("YES")                                 
f(n = int(input("Введите число больше 1: ")))
