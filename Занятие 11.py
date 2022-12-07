#Вариант 7 Репазиторий - Firehol IP Lists, ссылка - https://github.com/firehol/blocklist-ipsets
import json
import requests
from tkinter import*
def f(x):
    with open("C:\\Users\\USER\\.vscode\\extensions\\ms-python.python-2022.18.2\\languages\\shabanov", "w") as file:
        user = "ktsaou"
        url = f"https://api.github.com/users/{user}"
        user_data = requests.get(url).json()
        keys = ['id','url','name','company','email','created_at']
        data = user_data.keys()
        for i in data:
            if i in keys:
                file.write(f"{i}:{user_data[i]}" + '\n')

f(x  = int(input("Введите любое число: ")))
