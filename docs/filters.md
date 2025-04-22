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
```
