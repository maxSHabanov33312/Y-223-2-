def F(s):
    import re
    a = re.findall(r'\(.*?\)',s)
    print(a)
F(s = input("Введите текст: "))
