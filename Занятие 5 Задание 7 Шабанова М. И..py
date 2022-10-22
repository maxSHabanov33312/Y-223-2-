def F(x):   
    list = [x]
    y = 0
    while x != 0:
        list.append(x)
        x = int(input('>> '))
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            y += 1
    print(y)
F(x = int(input('Введите целые неотрицательные числа, '
              'для завершения введите 0:\n>> ')))
