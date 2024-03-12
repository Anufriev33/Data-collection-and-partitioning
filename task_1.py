#1.Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ 
#https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api
#2.Потренируйтесь делать запросы к API.Выберите публичный API,который вас интересует,и потренируйтесь делать API-запросы с помощью Postman.
#Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
#3.Сценарий Foursquare
#4.Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
#5.Используйте API Foursquare для поиска заведений в указанной категории.
#6.Получите название заведения, его адрес и рейтинг для каждого из них.
#7.Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.






#3.Сценарий Foursquare

import requests
import json


client_id = "__"
client_secret = "__"

# Конечная точка API
url = 'https://api.foursquare.com/v3/places/search?'





# Определение параметров для запроса API

categories= input("Ведите интересующую вас категорию : ")
city = input("Введите название города : ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": categories
}
headers = {
    "Accept": "application/json",
    "Authorization": "fsq30FHN6wrCFELxBa8Jc9gAn2QdYzI2bEPd8vaaGDt1cig="
}
response= requests.get(url, params=params,headers= headers)
if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    venues = data['results']
    for venue in venues:
        print('Название', venue['name'])
        print('Адрес', venue['location']['address'])
        
       
        
    print(f'Запрос не удался : код {response.status_code}')
    print(response.text)                 
   

   