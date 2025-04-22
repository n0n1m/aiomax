# Боты

## Инициализация бота

В aiomax используется класс `Bot` для работы с ботом.

Для примеров посмотрите в [examples.md](examples.md).

## Референс

### `Bot(access_token: str, command_prefixes: str | List[str] = '/', mention_prefix: bool = True, case_sensitive: bool = True, default_format: Literal['markdown', 'html'] | None = None)`

Создаёт объект класса `Bot`, через который можно управлять ботом.

- `access_token: str` - токен бота, взятый с [@MasterBot](https://max.ru/masterbot)

- `command_prefixes: str | List[str]` - префикс (или префиксы) команд бота. `/` по умолчанию

- `mention_prefix: bool` - будет ли бот реагировать на команды, начинающиеся с его имени пользователя (формата `@username /command`). Без `mention_prefix` бот не будет работать в группах. `True` по умолчанию.

- `case_sensitive: bool` - важна ли капитализация текста у команд. Например, если `False`, то команду с названием `test` можно будет ввести как и через `/test`, так и через `/TEST`. `True` по умолчанию.

- `default_format: 'markdown' | 'html' | None` - какой язык разметки использовать, если не указан в запросе. `None` по умолчанию.

### `Bot.get_me() -> User`

Возвращает объект класса `User` с информацией о профиле текущего бота.

### `Bot.patch_me(name: str | None, description: str | None, commands: List[BotCommand] | None, photo: ImageRequestPayload | None) -> User`

Изменяет информацию о боте и принимает параметры `name`, `description`, `commands`, `photo`.

Параметры, оставленные None (по умолчанию) не будут изменены.

Возвращает объект класса `User` с обновленными данными.

- `name: str | None` - новое имя бота

- `description: str | None` - новое описание профиля бота

- `commands: List[BotCommand] | None` - новый список команд бота

- `photo: ImageRequestPayload | None` - новая аватарка бота в виде объекта класса `ImageRequestPayload`

### `Bot.get_chats(count: int | None = None, marker: int | None = None) -> Chat`

Возвращает список объектов класса `Chat` с чатами в которых состоит бот.

- `count: int` - максимальное количество чатов на одной странице

- `marker: int` - маркер для смены страницы, который вы получили с другого вызова `get_chats`

### `Bot.chat_by_link(link: str)`

Возвращает объект класса `Chat` чата с указанной ссылкой

- `link: str` - ссылка на чат

### `Bot.get_chat(chat_id: int) -> Chat`

Возвращает объект класса `Chat` чата с указанным ID.

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

### `Bot.get_admins(chat_id: int) -> List[User]`

Возвращает список администраторов чата.

- `chat_id: int` - ID чата

### `Bot.get_members(chat_id: int) -> List[User]`

Возвращает список участников чата.

- `chat_id: int` - ID чата

### `Bot.add_members(chat_id: int, users: List[int])`

Добавляет в чат определенных пользователей.

- `chat_id: int` - ID чата

- `users: List[int]` - список ID пользователей, которых нужно добавить в чат

### `Bot.kick_member(chat_id: int, users: List[int])`

Удаляет пользователя из чата.

- `chat_id: int` - ID чата

- `user_id: int` - ID пользователя, которого нужно удалить из чата

- `block: bool | None` - Надо ли блокировать пользователя? False по умолчанию

### `Bot.patch_chat(chat_id: int, icon: ImageRequestPayload | None = None, title: str | None = None, pin: str | None = None, notify: bool | None = None)`

Изменяет информацию о чате, например имя, иконку или закрепленное сообщение (для последнего также есть `Bot.pin`).

Все аргументы, кроме `chat_id`, необязательны.

Возвращает объект класса Chat с обновленными данными о чате

- `chat_id: int` - ID чата

- `icon: ImageRequestPayload | None` - новая иконка чата в виде объекта класса `ImageRequestPayload`

- `title: str | None` - новое название чата

- `pin: str | None` - ID сообщения, которое нужно закрепить

- `notify: bool | None` - отправлять ли участникам чата уведомление об изменении чата

### `Bot.post_action(chat_id: int, action: str)`

Отправляет какое-либо действие бота в чат, например показывание иконки "печатает" или выставления галочки прочитывания сообщений.

- `chat_id: int` - ID чата

- `action: str` - нужное действие. Все возможные действия - `typing_on`, `sending_photo`, `sending_audio`, `sending_file`, `mark_seen` (также находятся в классе `Actions`)

### `Bot.upload(data: IO | str, type: str) -> dict`

Загружает файл с указанным типом на сервер и возвращает сырой JSON-объект, возвращенный сервисом хранения файлов.

**Не используйте эту функцию для загрузки файлов - для этого есть `upload_image`, `upload_video`, `upload_audio` и `upload_file`.**

- `data: IO | str` - Путь к файлу или file-like объект.

- `type: str` - Тип файла. `image`, `video`, `audio` или `file`.

### `Bot.upload_image(data: IO | str) -> PhotoAttachment`

Загружает картинку на сервер. Возвращает `PhotoAttachment`.

- `data: IO | str` - Путь к файлу или file-like объект.

### `Bot.upload_video(data: IO | str) -> VideoAttachment`

Загружает видео на сервер. Возвращает `VideoAttachment`.

- `data: IO | str` - Путь к файлу или file-like объект.

### `Bot.upload_audio(data: IO | str) -> AudioAttachment`

Загружает аудиофайл на сервер. Возвращает `AudioAttachment`.

- `data: IO | str` - Путь к файлу или file-like объект.

### `Bot.upload_file(data: IO | str) -> FileAttachment`

Загружает файл на сервер. Возвращает `FileAttachment`.

- `data: IO | str` - Путь к файлу или file-like объект.

### `Bot.send_message(text: str, chat_id: int | None = None, user_id: int | None = None, format: 'markdown' | 'html' | 'default' | None = 'default', reply_to: int | None = None, notify: bool = True, disable_link_preview: bool = False, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None)`

Отправляет сообщение в нужный чат.

- `text: str` - текст сообщения. Максимум 4000 символов

- `chat_id: int` - ID чата, куда отправить сообщение. Не может быть использован вместе с `user_id`

- `user_id: int` - ID пользователя, кому отправить сообщение. Не может быть использован вместе с `chat_id`

- `format: 'markdown' | 'html' | 'default' | None` - режим форматирования сообщения. `None` - без форматирования, `default` - режим форматирования по умолчанию (устанавливается при инициализации `Bot`). Необязательно

- `reply_to: int` - ID сообщения, на которое нужно ответить. Необязательно

- `notify: bool` - уведомлять ли пользователей о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - спрятать ли предпросмотр ссылок. `False` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - клавиатура, которую надо прикрепить к сообщению.

- `attachments: List[Attachment] | None` - список вложений, которые нужно прикрепить к сообщению

### `Bot.edit_message(message_id: int, text: "str | None" = None, format: 'markdown' | 'html' | 'default' | None = 'default', notify: bool = True, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None)`

Изменяет содержимое сообщения.

- `message_id: int` - сообщение для изменения

- `text: "str | None"` - текст сообщения. Максимум 4000 символов. Необязательно

- `format: 'markdown' | 'html' | 'default' | None` - режим форматирования сообщения. `None` - без форматирования, `default` - режим форматирования по умолчанию (устанавливается при инициализации `Bot`). Необязательно

- `reply_to: int` - ID сообщения, на которое нужно ответить. Необязательно

- `notify: bool` - уведомлять ли пользователей о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - спрятать ли предпросмотр ссылок. `False` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - новая клавиатура, которую надо прикрепить к сообщению. `None` не будет менять клавиатуру.

- `attachments: List[Attachment] | None` - новый список вложений. `None` не будет менять список файлов. Укажите `[]`, чтобы удалить все вложения - **это также удалит клавиатуру, если она есть**.

### `Bot.delete_message(message_id: int)`

Удаляет сообщение.

- `message_id: int` - ID сообщения для удаления.

### `Bot.start_polling()`

Начинает Long polling. Может использоваться обёрнутым в `asyncio.run()` в конце программы для запуска бота.

### `Bot.run()`

Начинает Long polling. Является коротким синтаксисом для `asyncio.run(Bot.start_polling())`.
