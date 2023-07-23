import requests

search_parameters = {
    "text": 'что такое backend',
    'lr': 213
}
url = 'https://yandex.ru/search/'
response = requests.get(url, params=search_parameters)
print(response.status_code)
print(response.url)