import requests

# Получение данных с сайта
response = requests.get('https://ru.wikipedia.org/wiki/Казань')

# Вывод статуса запроса
print(response.status_code)

# Вывод заголовков ответа
print(response.headers)

# Вывод содержимого ответа
print(response.text)