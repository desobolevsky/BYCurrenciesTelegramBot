import requests

from bs4 import BeautifulSoup

# scraping from finance.tut.by
page = requests.get("https://finance.tut.by/kurs/minsk/")
soup = BeautifulSoup(page.content, 'html.parser')

arr = soup.find_all('p')[4:-3]

d = ['Dollar', 'Euro', '100 RUB', '100 UAH', '10 PLN', 'Funt', 'Frank', '100 en', '100 CZK', '10 SWD', '100 CHN', 'CND']

for i, j in zip(range(0, len(arr), 4), d):
    print(j + ':', arr[i].string, arr[i + 1].string)

# scraping from myfin.by
page = requests.get("https://myfin.by/currency/minsk", headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(page.content, 'html.parser')

result = []

keys = ['USD_buy', 'USD_sell', 'EUR_buy', 'EUR_sell', '100RUB_buy', '100RUB_sell']
for el in soup.find_all('tr', class_='tr-tb'):
    html_tags = el.find_all('td')

    bank_data = {'bank_name': html_tags[0].contents[1].string}
    for i in range(len(keys)):
        bank_data[keys[i]] = float(html_tags[i + 1].contents[0])
    result.append(bank_data)

print(result)