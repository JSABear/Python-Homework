import requests

for i in range(5):
    p = "https://api.chucknorris.io/jokes/random"
    n = requests.get(p).json()
    print(n["value"])
