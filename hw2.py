import requests
city = "Moscow,RU"
appid = "26903477b329812d92afe3d0a1171e90"
s_city = "Москва"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")

for i in data['list']:
    print("____________________________")
    print("Дата <", i['dt_txt'], 
        "> \r\nТемпература <",
        '{0:+3.0f}'.format(i['main']['temp']), 
        "> \r\nПогодные условия <", i['weather'][0]['description'], 
        "> \r\nСкорость ветра <", i['wind']['speed'], 
        "> \r\nВидимость <", i['visibility'], ">")
print("____________________________")