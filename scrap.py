import requests

from bs4 import BeautifulSoup

page = requests.get("https://finance.tut.by/kurs/minsk/")
soup = BeautifulSoup(page.content, 'html.parser')

arr = soup.find_all('p')[4:-3]

d = ['Dollar', 'Euro', '100 RUB', '100 UAH', '10 PLN', 'Funt', 'Frank', '100 en', '100 CZK', '10 SWD', '100 CHN', 'CND']

for i, j in zip(range(0, len(arr), 4), d):
    print(j + ':', arr[i].string, arr[i + 1].string)
