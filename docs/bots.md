# Боты

## Инициализация бота

В aiomax используется класс `Bot` для работы с ботом.

Для начала нужно создать бота и получить его токен [в @MasterBot](https://max.ru/masterbot).

Для примеров посмотрите в [examples.md](examples.md).

## Референс

### `Bot(access_token: str, command_prefixes: str | list[str] = '/', mention_prefix: bool = True, case_sensitive: bool = True, default_format: Literal['markdown', 'html'] | None = None)`

Создаёт объект класса `aiomax.Bot`, через который можно управлять ботом.

`access_token: str` - токен бота, взятый с [@MasterBot](https://max.ru/masterbot)

`command_prefixes: str | list[str]` - префикс (или префиксы) команд бота. `/` по умолчанию

`mention_prefix: bool` - будет ли бот реагировать на команды, начинающиеся с его имени пользователя (формата `@username /command`). Без `mention_prefix` бот не будет работать в группах. `True` по умолчанию.

`case_sensitive: bool` - важна ли капитализация текста у команд. Например, если `False`, то команду с названием `test` можно будет ввести как и через `/test`, так и через `/TEST`. `True` по умолчанию.

`default_format: 'markdown' | 'html' | None` - какой язык разметки использовать, если не указан в запросе. `None` по умолчанию.

### `Bot.get_me() -> aiomax.User`

Метод возвращает объект класса `User` с информацией о профиле текущего бота.

### `Bot.patch_me(name: str | None, description: str | None, commands: list[aiomax.BotCommand] | None, photo: PhotoAttachmentRequestPayload | None) -> aiomax.User`

Метод изменяет информацию о боте и принимает параметры `name`, `description`, `commands`, `photo`.

Параметры, оставленные None (по умолчанию) не будут изменены.

Метод возвращает объект класса `User` с обновленными данными.
