import random #Доделать!!!
def f(n,m):    
    A = []
    a = 0
    b = 0
    c = 0
    for i in range(n):        
        A.append([random.sample(range(0, 10), m)])
    for i in A:
        for j in i:    
            print(j, end = ' ')
        print()
    for i in A:
        a = min(i)
        b = max(i)
        c = a
    a = b
    b = c
    for i in A:
        for j in i:    
            print(j, end = ' ')
        print()
f(n = 5, m = 5)
