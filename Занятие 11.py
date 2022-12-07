#Вариант 7 Репазиторий - Firehol IP Lists, ссылка - https://github.com/firehol/blocklist-ipsets
import json
import requests
def f(x):
    with open("shabanov", "w") as file:
        user = "ktsaou"
        url = f"https://api.github.com/users/{user}"
        user_data = requests.get(url).json()
        keys = ['id','url','name','company','email','created_at']
        data = user_data.keys()
        for i in data:
            if i in keys:
                print(file.write(f"{i}:{user_data[i]}" + '\n'), file.close)
        
f(x  = int(input("Введите любое число: ")))
