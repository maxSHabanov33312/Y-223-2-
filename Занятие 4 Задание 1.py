def F(A,B):
    C = B + 1
    if A <= C:
        for i in range(A,C):
            print(i,end=";")
    else:
        print("Условие неверно")
F(A = int(input()),B = int(input()))
