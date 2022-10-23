n = int(input("Введите длину массива "))
a = []
b = []
c = []
for i in range(n):
    print("Введите", i, "элемент")
    a.append(int(input()))
print(a)
for i in a:
    if a.count(i) > 1:
        b.append(i)
        c.append(a.index)
print(b)
print(c)
