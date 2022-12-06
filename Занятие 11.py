import requests
import json
from pprint import pprint
with open("C:\Users\USER\.vscode\extensions\shabanov","w") as file:
    url = f"https://github.com/kubernetes/kubernetes"
    data = requests.get(url).json()
    sh = ['company', 'created_at', 'email', 'id', 'name', 'url']
    data = data.keys()
    for i in data:
        if i in sh:
            file.write(f"{i}:{data[i]}" + '\n')
