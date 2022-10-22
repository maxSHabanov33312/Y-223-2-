def F(x):
    list = [x]
    while x != 0:
        list.append(x)
        x = int(input('>> '))
    s = len(list)
    print('Количество членов последовательности:', s - 1)
F(x = int(input('Введите целые неотрицательные числа, '
              'для завершения введите 0:\n>> ')))
