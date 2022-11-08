def f(k):
    a = k
    A = []
    while k>0:
        A.append(k%10)
        k=k//10
    b = len(A)
    s = sum(map(lambda x: x**b,A))
    return a == s        
for i in range(1,int(input())+1):
    if f(i):
        print(i)
