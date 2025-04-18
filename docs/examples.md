# Примеры

## Эхо-бот

```py
import aiomax
import asyncio

bot = aiomax.Bot('TOKEN')

@bot.on_message()
async def echo(message: aiomax.Message):
    await bot.reply(message.body.text, message)

asyncio.run(bot.start_polling())
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

asyncio.run(bot.start_polling())
```

## Эхо-бот с проверкой на чат

```py
import aiomax
import asyncio

bot = aiomax.Bot('TOKEN')

chat_id: int # Идентификатор чата, сообщение в котором должно обрабатыватся

@bot.on_message(lambda message: message.recipient.chat_id == chat_id)
async def test(message: aiomax.Message):
    await bot.send_message(message.body.text, message.recipient.chat_id)

asyncio.run(bot.start_polling())
```
