import requests
import time

from bs4 import BeautifulSoup

result = None
last_check_time = 0


# decorator which controls the updating of currencies
def updater(func):
    def wrapper():
        global result
        global last_check_time
        # update currencies only if 30 minutes passed
        if time.time() - last_check_time > 30 * 60:
            print('getting new info')
            last_check_time = time.time()
            result = func()
            return result
        else:
            return result

    return wrapper


# scraping from finance.tut.by
@updater
def scrap_general_currencies():
    page = requests.get("https://finance.tut.by/kurs/minsk/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # the first 4 and last 3 tags contains info that's not connected to rates,
    # that's why slicing from 4 to -3
    rates_tutby_scrapped = soup.find_all('p')[4:-3]

    # every 4 elements in rates_tutby_scrapped contain info about 1 currency
    # the 1st and 2nd elements are buy and sell rate, whereas 3rd and 4th are NBRB (НБРБ) rates,
    # that's why keep only 1st and 2nd for every 4 elements

    rates_tutby_clean = [rates_tutby_scrapped[i] for i in range(len(rates_tutby_scrapped)) if i % 4 == 0 or i % 4 == 1]

    currency_names = ['Dollar', 'Euro', '100 RUB', '100 UAH', '10 PLN', 'Funt', 'Frank', '100 en', '100 CZK', '10 SWD',
                      '100 CHN', 'CND']

    rates = {}
    for i in range(len(currency_names)):
        rates[currency_names[i]] = (rates_tutby_clean[i * 2].string, rates_tutby_clean[i * 2 + 1].string)

    return rates


# scraping from myfin.by
@updater
def scrap_bank_currencies():
    page = requests.get("https://myfin.by/currency/minsk", headers={'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.content, 'html.parser')

    rates = []

    keys = ['USD_buy', 'USD_sell', 'EUR_buy', 'EUR_sell', '100RUB_buy', '100RUB_sell']
    for el in soup.find_all('tr', class_='tr-tb'):
        html_tags = el.find_all('td')

        bank_data = {'bank_name': html_tags[0].contents[1].string}
        for i in range(len(keys)):
            bank_data[keys[i]] = float(html_tags[i + 1].contents[0])
        rates.append(bank_data)

    return rates
