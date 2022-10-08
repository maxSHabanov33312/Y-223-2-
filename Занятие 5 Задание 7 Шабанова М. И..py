x = int(input('Введите целые неотрицательные числа, '
              'для завершения введите 0:\n>> '))
lst = [x]
y = 0
while x != 0:
    lst.append(x)
    x = int(input('>> '))
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        y += 1
print(y)
