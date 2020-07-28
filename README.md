
# BYCurrenciesTelegramBot

BYCurrenciesTelegramBot is a telegram bot that shows exchange rates at present day in Belarus.
To launch the bot, follow the link - https://t.me/BY_Currencies_bot, or write to the bot directly in Telegram - @BY_Currencies_bot .


<p><img align = "center" src = "https://i.ibb.co/JxYMXGw/IMG-6952.png" width ="250"/> <img align = "center" src = "https://i.ibb.co/R3npLN3/IMG-6953.png" width ="250"/> <img align = "center" src = "https://i.ibb.co/t81DRfK/IMG-6955.png" width ="250"/></p>


# Description
In dialog with the bot, you can use these commands to interact with it:

  - /general - for general overview of exchange rates at present day
  - /banks - for detailed list of exchange rate for each bank
  - /help - if you need any kind of help ;) 

Currencies are parsed from [finance.tut.by](https://finance.tut.by/kurs/minsk/) and  [myfin.by](https://myfin.by/currency/minsk) websites.

Note: exchange rates are updated no more than every 30 minutes (depends on bot users activity).

## Tech
BYCurrenciesTelegramBot uses a number of open source projects to work properly:

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - package for parsing HTML and XML documents.
* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - simple, but powerful Python wrapper for the [Telegram Bot API](https://core.telegram.org/bots/api).
* [PyYAML](https://github.com/yaml/pyyaml) - YAML parser and emitter for Python.

## Installation

In order to get the project for review, editing or testing, clone project:
```sh
$ git clone https://github.com/desobolevsky/BYCurrenciesTelegramBot.git
```

Create a new virtual environment and install the dependencies:

```sh
$ cd BYCurrenciesTelegramBot
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Create your bot in Telegram via interacting with [@BotFather](https://t.me/BotFather) and get API key for your bot (see https://core.telegram.org/bots#6-botfather for more information).

Rename config.yaml.dist file to config.yaml:
```sh
$ mv config.yaml.dist config.yaml
```
Paste your API key to config.yaml so the file looks as follows:
```
api_key: YOUR_API_KEY_HERE
```

Run the bot:

```sh
$ python3 main.py
```

Your bot started, now you can enjoy exchange rates in Belarus! :)


## Todos

 - Add sorted exchange rates, so that the best ones are displayed first
 - Add statistics
 - Add daily notifications 

