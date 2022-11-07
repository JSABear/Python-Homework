import requests


API_key = "536025f917f606d3f38261ae0276b78c"
lat = []
lon = []

user_input = input("Anna paikkakunnan nimi: ")

city = f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit={1}&appid={API_key}"
try:
    value = requests.get(city)
    if value.status_code == 200:
        json_value = value.json()
        for i in json_value:
            lat = i["lat"]
            lon = i["lon"]
except requests.exceptions.RequestException as e:
    print("Virheellinen valinta.")


weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
try:
    final_weather = requests.get(weather)
    if final_weather.status_code == 200:
        final = final_weather.json()
        final_main = final["main"]
        final_temp = final_main["temp"]
        print(f"{final_temp}\u00b0")
except requests.exceptions.RequestException as e:
    print("Virheellinen valinta.")