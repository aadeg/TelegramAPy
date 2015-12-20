[![Build Status](https://travis-ci.org/aadeg/telegramapi.svg?branch=master)](https://travis-ci.org/aadeg/telegramapi)
# TelegramAPy
A simple library for interacting with the [Telegram Bot API](https://core.telegram.org/bots/api).

## Usage
Use this library is pretty straightfoward. First you have to create a new instance of TelegramAPy passing the token generated by Telegram:
```python
from telegramapi.telegram.api import TelegramAPy

token = "TokenGeneratedByTelegram"
api = TelegramAPy(token)
```

Now that you have created the instace, you can call all the methods defined in the [Telegram Bot API](https://core.telegram.org/bots/api) page.

This library is updated with the changes of November, 2015.
