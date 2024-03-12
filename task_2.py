#Задача №2 Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех категориях: 
#название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
#Затем сохранить эту информацию в JSON-файле.

# Решение 


import requests
from bs4 import BeautifulSoup
import json


url ='http://books.toscrape.com'


# Функция для извлечения данных о книгах
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = []
    
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = float(book.find('p', class_='price_color').get_text().replace('£', '').replace('Â', ''))
        
        availability = book.find('p', class_='instock availability').get_text().strip()
        
        description = book.p['class'][0].capitalize()
        
        books.append({
            'title': title,
            'price': price,
            'availability': availability,
            'description': description
        })
    
    return books

# Извлечение данных всех книг во всех категориях
all_books = []

base_url = 'http://books.toscrape.com/catalogue/'
page_num = 1
while True:
    url = f'{base_url}page-{page_num}.html'
    response = requests.get(url)
    
    if response.status_code == 200:
        all_books.extend(scrape_books(url))
        page_num += 1
    else:
        break

# Сохранение данных в JSON-файл
with open('books_data.json', 'w') as file:
    json.dump(all_books, file, indent=4)

print('Данные успешно сохранены в books_data.json')




