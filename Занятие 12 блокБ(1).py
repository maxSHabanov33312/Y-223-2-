def f(x):
    b = int(input("Вводите числа. Для завершения введите 0 "))
    if b != 0:
        x.append(b)
        return f(x)
    else:        
        s = print(max(x))
        return s
f(x = [])
