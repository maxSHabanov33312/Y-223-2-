import random
def F(n,m):
    A = [[random.randrange(10) for i in range(m)] for j in range(n)]
    print(A)
    for i, row in enumerate(A):
        max = min = 0
        for j, elem in enumerate(row):
            if elem > row[max]:
                max = j
            if elem < row[min]:
                min = j
        row[max], row[0] = row[0], row[max]
        row[min], row[-1] = row[-1], row[min]
    print(A)
F(n = 5, m = 5)
