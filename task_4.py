# Задание № 4

# Выберите веб-сайт с табличными данными, который вас интересует.
# Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
# Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
# Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

# Ваш код должен включать следующее:

# Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
# Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
# Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
# Комментарии для объяснения цели и логики кода.

# Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге

# Решение:


import requests
from lxml import html
import csv

# URL сайта с табличными данными
url = 'https://coinmarketcap.com/'

# Заголовок HTTP-запроса с пользовательским агентом
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Отправка HTTP GET-запроса
response = requests.get(url, headers=headers)

# Проверка успешности запроса
if response.status_code == 200:
    # Получение содержимого страницы
    page_content = html.fromstring(response.content)
    
    # Выражение XPath для таблицы с данными криптовалют
    table_rows = page_content.xpath('//table[contains(@class, "cmc-table")]/tbody/tr')
    
    # Создание CSV-файла для сохранения данных
    with open('crypto_data1.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Запись заголовков столбцов
        writer.writerow(['Rank', 'Name', 'Price', 'Market Cap', 'Volume', 'Change'])
        
        # Извлечение данных из таблицы и запись в CSV
        for row in table_rows:
            rank = row.xpath('.//td[1]//text()')
            name = row.xpath('.//td[2]//p/text()')
            price = row.xpath('.//td[3]//a/text()')
            market_cap = row.xpath('.//td[4]//text()')
            volume = row.xpath('.//td[5]//text()')
            change = row.xpath('.//td[6]//text()')
            
            if rank and name and price and market_cap and volume and change:
                writer.writerow([rank[0].strip() if rank else "", name[0].strip() if name else "", price[0].strip() if price else "", market_cap[0].strip() if market_cap else "", volume[0].strip() if volume else "", change[0].strip() if change else ""])
            
    print("Данные успешно сохранены в файл crypto_data1.csv.")
else:
    print("Ошибка при получении данных. Статус код:", response.status_code)
