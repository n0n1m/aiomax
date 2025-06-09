# Примеры

## Инициализация бота

Для начала нужно создать бота и получить его токен [в @MasterBot](https://max.ru/masterbot).

Этот токен нужно вставить везде, где написано `'TOKEN'`.

## Эхо-бот

```py
import aiomax
import asyncio

bot = aiomax.Bot('TOKEN')

@bot.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.body.text)

bot.run()
```

## Генератор рандомных чисел

```py
import aiomax
import asyncio
import random

bot = aiomax.Bot('TOKEN', default_format='markdown')

# Команда для генерации случайных чисел: /random минимум максимум
@bot.on_command('random', aliases=['rnd'])
async def gen(ctx: aiomax.CommandContext):
    try:
        min_num = int(ctx.args[0])
        max_num = int(ctx.args[1])
        number = random.randint(min_num, max_num)
    except:
        await ctx.reply('❌ **Некорректные аргументы!**\n\n/random <миниммум> <максимум>')
        return

    await ctx.reply(f'Ваше число: **{number}**')

# Сообщение при начале чата с ботом
@bot.on_bot_start()
async def on_bot_start(payload: aiomax.BotStartPayload):
    await bot.send_message('**Моя команда:**\n\n/random <минимум> <максимум>', payload.chat_id)

# Отправляет команды на сервер, чтобы они отображались у пользователей в меню
@bot.on_ready()
async def send_commands():
    await bot.patch_me(commands=[
        aiomax.BotCommand('random', 'Генерирует случайное число от минимума до максимума')
    ])

bot.run()
```

## Эхо-бот с проверкой на чат

```py
import aiomax
import asyncio

bot = aiomax.Bot('TOKEN')

chat_id: int = 2409 # ID чата, сообщения в котором должны обрабатыватся

@bot.on_message(lambda message: message.recipient.chat_id == chat_id)
async def echo(message: aiomax.Message):
    await bot.send_message(message.body.text, message.recipient.chat_id)

bot.run()
```

## Простой счётчик со сбросом

```py
import aiomax
import asyncio

bot = aiomax.Bot('TOKEN')
taps = 0

# Команда отправляющая сообщение с кнопками
@bot.on_command('tap')
async def tap_command(ctx: aiomax.CommandContext):
    kb = aiomax.buttons.KeyboardBuilder()
    kb.add(aiomax.buttons.CallbackButton('Тап', 'tap'))
    kb.row(aiomax.buttons.CallbackButton('Сбросить', 'reset'))

    await ctx.reply(f'Тапов: {taps}', keyboard=kb)

# Обработчик кнопки "Тап" (увеличение счетчика)
@bot.on_button_callback(lambda data: data.payload == 'tap')
async def tap(cb: aiomax.Callback):
    global taps
    taps += 1
    await cb.answer(text=f'Тапов: {taps}', format='markdown')

# Обработчик кнопки "Сбросить" (сброс счетчика)
@bot.on_button_callback(lambda data: data.payload == 'reset')
async def reset(cb: aiomax.Callback):
    global taps
    taps = 0
    await cb.answer('Вы сбросили все тапы!', text=f'Тапов: {taps}')

bot.run()
```

## Разделение на несколько файлов через роутеры

### `echo.py`

```py
import aiomax

router = aiomax.Router()

@router.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)
```

### `main.py`

```py
import aiomax
import echo

bot = aiomax.Bot('TOKEN')
bot.add_router(echo.router)

bot.run()
```

## Глобальные фильтры

```py
import aiomax

bot = aiomax.Bot('TOKEN')
command_router = aiomax.Router()
command_router.add_message_filter(aiomax.filters.startswith('$'))

# эти функции сработают только если сообщение начинается с '$'

@command_router.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)

@command_router.on_message()
async def name(message: aiomax.Message):
    await message.reply(message.sender.name)

# эта функция сработает всегда

@bot.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)

bot.add_router(command_router)
bot.run()
```

## Ввод имени и фамилии с помощью FSM

```py
import aiomax
from aiomax import fsm

bot = aiomax.Bot('TOKEN')


# Запуск бота пользователем
@bot.on_bot_start()
async def start(pd: aiomax.BotStartPayload, cursor: fsm.FSMCursor):
    await pd.send("Как Вас зовут?")
    cursor.change_state('name')  # Изменения состояние


# Ввод имени
@bot.on_message(aiomax.filters.state('name'))
async def write_name(message: aiomax.Message, cursor: fsm.FSMCursor):
    await message.reply("Напишите свою фамилию")
    cursor.change_state('surname')  # Изменения состояние
    cursor.change_data({'name': message.content})  # Добавление имени в данные


@bot.on_message(aiomax.filters.state('surname'))
async def write_surname(message: aiomax.Message, cursor: fsm.FSMCursor):
    name = cursor.get_data()['name']  # Получение имени из данных
    surname = message.content

    await message.reply(f"Здравствуйте, {name} {surname}")
    cursor.clear()  # Очищение состояния и данных пользователя

bot.run()
```

## Остальная документация

- [Функции класса `Bot`](bots.md)

- [Декораторы и хендлеры](decorators.md)

- [Кнопки и клавиатуры](buttons.md)

- [Классы](classes.md)

- [Логирование](logging.md)

- [FSM (Конечные автоматы)](fsm.md)

- [Фильтры](filters.md)

- [Роутеры](routers.md)
