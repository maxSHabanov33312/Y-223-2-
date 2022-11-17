import random
def f():
    print("Задание 1")
    file = open('C:\\Users\\USER\\Desktop\\Шабанов_М_И_У-223_vvod.txt', 'r')
    file2 = open('C:\\Users\\USER\\Desktop\\Шабанов_М_И_У-223_vivod1.txt', 'w')
    n = int(file.readline())
    m = int(file.readline())
    n = int(n)
    m = int(m)
    A = []
    for i in range(n):
        A.append([random.sample(range(0, 9999999999999999), m)])
    for i in A:
        for j in i:
            print(j, end=' ')
        print()
    for i in A:
        for j in i:
            print(min(j), end=' ')
        print()
    for i in range(len(A)):
        file2.write(str(A[i]) + '\n')
f()
def s():
    print("Задание 2")
    file = open('C:\\Users\\USER\\Desktop\\Шабанов_М_И_У-223_vvod.txt', 'r')
    file2 = open('C:\\Users\\USER\\Desktop\\Шабанов_М_И_У-223_vivod1.txt', 'w')
    A = [[random.randrange(10) for i in range(5)] for j in range(5)]
    n = int(file.readline(A))
    for i, row in enumerate(A):
        max = min = 0
        for j, elem in enumerate(row):
            if elem > row[max]:
                max = j
            if elem < row[min]:
                min = j
        row[max], row[0] = row[0], row[max]
        row[min], row[-1] = row[-1], row[min]
    for i in range(len(A)):
        file2.write(str(A[i]) + '\n')
s()
