import random
def f(n,m):    
    A = []
    for i in range(n):        
        A.append([random.sample(range(0, 9999999999999999), m)])
    for i in A:
        for j in i:    
            print(j, end = ' ')
        print()
    for i in A:
        for j in i:     
            print(min(j), end = ' ')
        print()
f(n = int(input()),m = int(input()))
