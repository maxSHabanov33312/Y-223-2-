n = int(input())
a = 1
b = 1
for i in range(2,n+1):
    a = a * i
    b += a
print(b)
