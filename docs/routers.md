# Роутеры

Роутер - `aiomax.Router` - это класс, который содержит только обработчики событий ([декораторы](decorators.md)), и который добавляется к основному классу `aiomax.Bot`.

Роутеры могут быть полезны, если вы хотите разделить ваш код на несколько файлов.

Пример разделенного на файлы бота можно посмотреть [тут](examples.md).

## Создание

Для создания роутера создаём экземпляр класса `aiomax.Router`:

```py
router = aiomax.Router()
```

Добавлять обработчиков в него можно точно также, как и в класс `aiomax.Bot`, например:

```py
@router.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)
```

Чтобы роутер работал, его нужно присвоить к основному классу `aiomax.Bot`:

```py
bot = aiomax.Bot('TOKEN')
bot.add_router(router)
bot.run()
```

В итоге получаем:

```py
import aiomax

bot = aiomax.Bot('TOKEN')
router = aiomax.Router()

@router.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)

bot.add_router(router)
bot.run()
```

Это - эквивалент кода:

```py
import aiomax

bot = aiomax.Bot('TOKEN')

@bot.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)

bot.run()
```

Если ваш роутер находится в отдельном файле, где нет доступа к главному классу `aiomax.Bot`, вы можете получить его через `router.bot`:

```py
@router.on_command('my_name')
async def my_name(message: aiomax.Message):
    await message.reply('Мое имя - '+router.bot.name)
```

Так как `add_router` - функция класса `aiomax.Router`, а `aiomax.Router` - это суперкласс `aiomax.Bot`, вы можете использовать её как и на боте, так и на другом роутере.

```py
bot = aiomax.Bot('TOKEN')

# роутер-родитель
router = aiomax.Router()

@router.on_message()
async def echo(message: aiomax.Message):
    await message.reply(message.content)

bot.add_router(router)

# второй роутер
child_router = aiomax.Router()

@child_router.on_message()
async def echo_second(message: aiomax.Message):
    await message.reply(message.content)

router.add_router(child_router)
```
