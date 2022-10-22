def F(x,y):
    d = 1
    while x < y:
        x = x*1.1
        d+=1
    print(d)
F(x = int(input()),y = int(input()))
