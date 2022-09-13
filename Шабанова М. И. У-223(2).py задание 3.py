age = int(input())
name = input()
if age > 0 and age < 75:
    if name == "Иван":
        print("Ивану вход воспрещён!!!")
    else:
        if age > 16:
            print("Поздровляем, Вы поступили во ВГУИТ!")
        else:
            print("Сначала нужно окончить школу!")
else:
    print("Нужно ввести корректный возраст!")