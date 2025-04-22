# Фильтры

## Написание собственных фильтров

При написании собственных фильтров у вас есть 3 варианта:

### lambda-функция

Самый короткий вариант для небольших фильтров. Используется в одну строку.
Пример для проверки на то, что сообщение отправлено в диалоге:

```python
@bot.on_message(lambda message: message.recipient.chat_type == 'dialog')
async def dialog(message: aiomax.Message):
    pass # Содержимое функции
```

### def-функция

Использование def-функций занимает больше места, но помогает избежать повторов кода, если один и тот же фильтр используется несколько раз.

Пример для проверки на то, что сообщение отправлено в диалоге

```python
def in_dialog(message: aiomax.Message):
    return message.recipient.chat_type == 'dialog'

@bot.on_message(in_dialog)
async def dialog(message: aiomax.Message):
    pass # Содержимое функции
```

### Классы

Классы используются для более сложных фильтров, принимающих аргументы
Пример фильтра, принимающего тип чата и проверяющего, что сообщение отправлено именно в чате этого типа

```python
class ChatTypeFilter:
    def __init__(self, chat_type):
        self.chat_type = chat_type

    def __call__(self, message: aiomax.Message):
        return message.recipient.chat_type == self.chat_type

@bot.on_message(ChatTypeFilter('dialog'))
async def dialog(message: aiomax.Message):
    pass # Содержимое функции
```

## Встроенные фильтры

В подмодуле `aiomax.filters` есть несколько встроенных фильтров.

### aiomax.filters.startswith(prefix: str)

- `prefix` - Строка, с которой должен начинаться контент

Фильтр проверяет, чтобы контент начинался с префикса

### aiomax.filters.regex(pattern: str)

- `pattern` - Регулярное выражение

Фильтр проверяет, чтобы контент соответствовал регулярному выражению
