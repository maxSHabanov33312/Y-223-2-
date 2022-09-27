d = 0
def add(a,b,c):
    if a==b and b==c and a==c:
        d = 3
    else:
        if a==b or b==c or a==c:
            d = 2
        else:
            d = 0
    print(d)
add(a = int(input()), b = int(input()), c = int(input()))
