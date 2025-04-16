# Боты

## Инициализация бота

В aiomax используется класс `Bot` для работы с ботом.

Для начала нужно создать бота и получить его токен [в @MasterBot](https://max.ru/masterbot).

Для примеров посмотрите в [examples.md](examples.md).

## Референс

### `Bot(access_token: str, command_prefixes: str | list[str] = '/', mention_prefix: bool = True, case_sensitive: bool = True, default_format: Literal['markdown', 'html'] | None = None)`

Создаёт объект класса `aiomax.Bot`, через который можно управлять ботом.

- `access_token: str` - токен бота, взятый с [@MasterBot](https://max.ru/masterbot)

- `command_prefixes: str | list[str]` - префикс (или префиксы) команд бота. `/` по умолчанию

- `mention_prefix: bool` - будет ли бот реагировать на команды, начинающиеся с его имени пользователя (формата `@username /command`). Без `mention_prefix` бот не будет работать в группах. `True` по умолчанию.

- `case_sensitive: bool` - важна ли капитализация текста у команд. Например, если `False`, то команду с названием `test` можно будет ввести как и через `/test`, так и через `/TEST`. `True` по умолчанию.

- `default_format: 'markdown' | 'html' | None` - какой язык разметки использовать, если не указан в запросе. `None` по умолчанию.

### `Bot.get_me() -> aiomax.User`

Возвращает объект класса `User` с информацией о профиле текущего бота.

### `Bot.patch_me(name: str | None, description: str | None, commands: list[aiomax.BotCommand] | None, photo: PhotoAttachmentRequestPayload | None) -> aiomax.User`

Изменяет информацию о боте и принимает параметры `name`, `description`, `commands`, `photo`.

Параметры, оставленные None (по умолчанию) не будут изменены.

Возвращает объект класса `User` с обновленными данными.

### `Bot.get_chats(count: int | None = None, marker: int | None = None) -> dict`

Возвращает (пока что) словарь с данными чатов, в которых находится бот.

- `count: int` - максимальное количество чатов на одной странице

- `marker: int` - маркер для смены страницы, который вы получили с другого вызова `get_chats`

### `Bot.get_chat(chat_id: int) -> dict`

Возвращает (пока что) словарь с данными чата с указанным ID.

- `chat_id: int` - ID чата

### `Bot.get_pin(chat_id: int) -> Message | None`

Возвращает объект класса `Message` с закрепленным сообщением, или `None`, если в чате нет закрепленных сообщений.

- `chat_id: int` - ID чата, в котором нужно посмотреть закрепленное сообщение

### `Bot.pin(chat_id: int, message_id: str, notify: bool | None = None)`

Закрепляет сообщение в чате.

- `chat_id: int` - ID чата, в котором нужно закрепить сообщение

- `message_id: str` - ID сообщения, которое нужно закрепить

- `notify: bool | None` - уведомлять ли пользователей о закреплении сообщения. `True` по умолчанию

### `Bot.delete_pin(chat_id: int)`

Удаляет закрепленное сообщение в чате.

- `chat_id: int` - ID чата

### `Bot.my_membership(chat_id: int) -> User`

Возвращает объект класса `User` с информацией о боте в том или ином чате.

- `chat_id: int` - ID чата

### `Bot.leave_chat(chat_id: int)`

Заставляет бота покинуть тот или иной чат.

- `chat_id: int` - ID чата

### `Bot.get_admins(chat_id: int) -> list[User]`

Возвращает список администраторов чата.

- `chat_id: int` - ID чата

### `Bot.get_members(chat_id: int) -> list[User]`

Возвращает список участников чата.

- `chat_id: int` - ID чата

### `Bot.add_members(chat_id: int, users: list[int])`

Добавляет в чат определенных пользователей.

- `chat_id: int` - ID чата

- `users: list[int]` - список ID пользователей, которых нужно добавить в чат

### `Bot.kick_member(chat_id: int, users: list[int])`

Удаляет пользователя из чата.

- `chat_id: int` - ID чата

- `user_id: int` - ID пользователя, которого нужно удалить из чата
- `block: bool | None` - Надо ли блокировать пользователя? False по умолчанию

### `Bot.patch_chat(chat_id: int, icon: PhotoAttachmentRequestPayload | None = None, title: str | None = None, pin: str | None = None, notify: bool | None = None)`

Изменяет информацию о чате, например имя, иконку или закрепленное сообщение (для последнего также есть `Bot.pin`).

Все аргументы, кроме `chat_id`, необязательны.

- `chat_id: int` - ID чата

- `icon: PhotoAttachmentRequestPayload | None` - новая иконка чата

- `title: str | None` - новое название чата

- `pin: str | None` - ID сообщения, которое нужно закрепить

- `notify: bool | None` - отправлять ли участникам чата уведомление об изменении чата

### `Bot.post_action(chat_id: int, action: str)`

Отправляет какое-либо действие бота в чат, например показывание иконки "печатает" или выставления галочки прочитывания сообщений.

- `chat_id: int` - ID чата

- `action: str` - нужное действие. Все возможные действия - `typing_on`, `sending_photo`, `sending_audio`, `sending_file`, `mark_seen` (также находятся в классе `Actions`)

### `Bot.send_message(text: str, chat_id: int | None = None, user_id: int | None = None, format: 'markdown' | 'html' | 'default' | None = 'default', reply_to: int | None = None, notify: bool = True, disable_link_preview: bool = False)`

Отправляет сообщение в нужный чат.

- `text: str` - текст сообщения. Максимум 4000 символов

- `chat_id: int` - ID чата, куда отправить сообщение. Не может быть использован вместе с `user_id`

- `user_id: int` - ID пользователя, кому отправить сообщение. Не может быть использован вместе с `chat_id`

- `format: 'markdown' | 'html' | 'default' | None` - режим форматирования сообщения. `None` - без форматирования, `default` - режим форматирования по умолчанию (устанавливается при инициализации `Bot`). Необязательно

- `reply_to: int` - ID сообщения, на которое нужно ответить. Необязательно

- `notify: bool` - уведомлять ли пользователей о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - спрятать ли предпросмотр ссылок. `False` по умолчанию

### `Bot.reply(text: str, message: Message, format: 'markdown' | 'html' | 'default' | None = 'default', notify: bool = True, disable_link_preview: bool = False)`

Отправляет ответ на сообщение. Сделано как небольшое упрощение ответа на сообщения через `Bot.send_message`.

- `text: str` - текст сообщения. Максимум 4000 символов

- `message: Message` - сообщение, на которое нужно ответить

- `format: 'markdown' | 'html' | 'default' | None` - режим форматирования сообщения. `None` - без форматирования, `default` - режим форматирования по умолчанию (устанавливается при инициализации `Bot`). Необязательно

- `notify: bool` - уведомлять ли пользователей о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - спрятать ли предпросмотр ссылок. `False` по умолчанию

### `Bot.edit_message(message_id: int, text: str, format: 'markdown' | 'html' | 'default' | None = 'default', notify: bool = True)`

Изменяет содержимое сообщения.

- `message_id: int` - сообщение для изменения

- `text: str` - текст сообщения. Максимум 4000 символов

- `format: 'markdown' | 'html' | 'default' | None` - режим форматирования сообщения. `None` - без форматирования, `default` - режим форматирования по умолчанию (устанавливается при инициализации `Bot`). Необязательно

- `reply_to: int` - ID сообщения, на которое нужно ответить. Необязательно

- `notify: bool` - уведомлять ли пользователей о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - спрятать ли предпросмотр ссылок. `False` по умолчанию

### `Bot.delete_message(message_id: int)`

Удаляет сообщение.

- `message_id: int` - ID сообщение для удаления.
