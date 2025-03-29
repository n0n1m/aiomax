# Боты

## Инициализация бота
В aiomax используется класс `Bot` для работы с ботом
Для начала нужно получить создать бота и получить его токен [в @MasterBot](https://max.ru/masterbot)

```python
import aiomax

token = "BOT_TOKEN" # Токен бота

bot = aiomax.Bot(token) # Объявление объекта класса Bot
```

## Долгий опрос (long polling)
Чтобы бот хендлил все обновления, используется метод `long_polling`
Он создает сессию и бесконечный цикл. Для хендлинга используются декораторы (Подробнее в [decorators.md](/docs/decorators.md))

```python
import aiomax

token = "BOT_TOKEN" # Токен бота

bot = aiomax.Bot(token) # Объявление объекта класса Bot

# Хендлеры

if __name__ == "__main__":
    asyncio.run(bot.start_polling())
```

## Bot.get_me
Метод возвращает объект класса `User` с информацией о текущем боте

```python
import aiomax

token = "BOT_TOKEN" # Токен бота

bot = aiomax.Bot(token) # Объявление объекта класса Bot

@bot.on_ready() # Декоратор, который вызывается при запуске бота
async def main():
    print(await bot.get_me())

asyncio.run(bot.start_polling())
```

# Bot.patch_me
Метод изменяет информацию о боте и принимает параметры `name`, `description`, `commands`, `photo`
Параметры, оставленные None (по умолчанию) не будут изменены
Метод возвращает объект класса User с обновленными данными

```python
import aiomax

token = "BOT_TOKEN" # Токен бота

bot = aiomax.Bot(token) # Объявление объекта класса Bot

@bot.on_ready() # Декоратор, который вызывается при запуске бота
async def main():
    print(await bot.patch_me(name="new name")) # Изменяет имя бота на new_name

asyncio.run(bot.start_polling())
```