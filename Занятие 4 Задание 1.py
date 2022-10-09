A = int(input())
B = int(input())
C = B + 1
if A <= C:
    for i in range(A,C):
        print(i,end=";")
else:
    print("Условие неверно")
