def a(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
 
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
res = [x1, x2]
ax = a(x1, x2)
ay = a(y1, y2)
if ay > ax :
    ax = ay
    res = [y1, y2]
az = a(z1, z2)
if az > ax :
    az = az
    res = [z1, z2]
print(*res)
