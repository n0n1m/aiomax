# Классы

## `BotCommand`

Команда бота. Нужна для обновления списка команд в боте.

- `name: str` - название команды

- `description: str` - описание команды

## `User`

Пользователь Max.

- `user_id: int` - ID пользователя

- `first_name: str` - имя пользователя

- `last_name: str` - фамилия пользователя

- `name: str` - полное имя пользователя (имя + фамилия)

- `is_bot: bool` - является ли пользователь ботом

- `last_activity_time: int` - время последней активности пользователя

- `username: str | None` - @username пользователя. Может быть `None`

- `description: str | None` - описание пользователя. Может быть `None`

- `avatar_url: str | None` - ссылка на thumbnail аватара пользователя. Может быть `None`

- `full_avatar_url: str | None` - ссылка на аватар пользователя. Может быть `None`

- `commands: List[BotCommand] | None` - список команд бота. Не `None` только если `User` получен через `Bot.get_me()`

- `last_access_time: int | None` - время последней активности пользователя в чате. Не `None` только если `User` получен через метод, связанный с каким-либо чатом.

- `is_owner: bool | None` - является ли пользователь владельцем чата. Не `None` только если `User` получен через метод, связанный с каким-либо чатом.

- `is_admin: bool | None` - является ли пользователь администратором чата. Не `None` только если `User` получен через метод, связанный с каким-либо чатом.

- `join_time: int | None` - время присоединения пользователя к чату. Не `None` только если `User` получен через метод, связанный с каким-либо чатом.

- `permissions: List[str] | None` - список разрешений пользователя в чате. Не `None` только если `User` получен через метод, связанный с каким-либо чатом.

### `User.__eq__()`

Сравнение двух классов `User` сравнивает их `User.user_id`.

## `MediaPayload`

Информация о вложении медиа.

- `token: str` - токен вложения

- `url: str | None` - ссылка на вложение. Может быть `None`

### `PhotoPayload`

Информация о вложении фото. Суперкласс `MediaPayload`, содержит дополнительное поле:

- `photo_id: int | None` - ID фото. Может быть `None`

## `StickerPayload`

Информация о стикере.

- `url: str` - ссылка на изображение стикера

- `code: str` - код стикера

## `ContactPayload`

Информация о контакте.

- `vcf_info: str | None` - информация о пользователе в формате VCF

- `max_info: User | None` - пользователь Max

## `Attachment`

Вложение сообщения. Имеет несколько типов.

### `PhotoAttachment`

Вложение фото.

- `payload: PhotoPayload` - информация о вложении

### `VideoAttachment`

Вложение видео.

- `payload: MediaPayload` - информация о вложении

- `thumbnail: str | None` - ссылка на thumbnail. Может быть `None`

- `width: int | None` - ширина видео. Может быть `None`

- `height: int | None` - высота видео. Может быть `None`

- `duration: int | None` - продолжительность в секундах. Может быть `None`

### `AudioAttachment`

Вложение аудио.

- `payload: MediaPayload` - информация о вложении

- `transcription: str | None` - транскрипция аудио. Может быть `None`

### `FileAttachment`

Вложение файла.

- `payload: MediaPayload` - информация о вложении

- `filename: str | None` - имя файла. Может быть `None`

- `size: int | None` - размер файла в байтах. Может быть `None`

### `StickerAttachment`

Вложение стикера.

- `payload: StickerPayload` - информация о вложении

- `width: int | None` - ширина стикера. Может быть `None`

- `height: int | None` - высота стикера. Может быть `None`

### `ContactAttachment`

Вложение контакта.

- `payload: ContactPayload` - информация о вложении

### `ShareAttachment`

Предпросмотр ссылки.

- `payload: MediaPayload | None` - информация о вложении. Может быть `None`. `url` в `MediaPayload` в этом случае является ссылкой, прикрепленной к сообщению в качестве предпросмотра медиа.

- `title: str | None` - заголовок предпросмотра ссылки. Может быть `None`

- `description: str | None` - описание предпросмотра ссылки. Может быть `None`

- `image_url: str | None` - ихображение предпросмотра ссылки. Может быть `None`

### `LocationAttachment`

Вложение геолокации.

- `latitude: float` - широта

- `longitude: float` - долгота

### `InlineKeyboardAttachment`

Вложение инлайн-клавиатуры.

- `payload: List[List[buttons.Button]]` - двумерный массив кнопок в виде объектов `buttons.Button`

## `Message`

Информация об отправленном сообщении.

- `recipient: MessageRecipient` - информация о получателе

- `body: MessageBody` - информация о содержимом сообщения

- `timestamp: float` - время отправки

- `sender: User` - отправитель

- `link: LinkedMessage | None` - пересланное сообщение или сообщение, на которое ответили. Может быть `None`

- `views: int | None` - количество просмотров. Может быть `None`

- `url: str | None` - публичная ссылка на сообщение. Может быть `None` для не публичных чатов или ЛС

- `id: str` - ID сообщения. Возвращает `Message.body.message_id`

- `user_locale: str | None` - язык пользователя в формате IETF BCP 47. Доступен только в ЛС

### `Message.__eq__()`

Сравнение двух классов `Message` сравнивает их `Message.id`.

### `Message.__str__()`

Возвращает `Message.body.text`.

### `Message.send(text: str, format: Literal['html', 'markdown', 'default'] | None = 'default', notify: bool = True, disable_link_preview: bool = False, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None) -> Message`

Отправляет сообщение в чат, в который было отправлено сообщение.

- `text: str` - текст сообщения. Максимум 4000 символов

- `format: Literal['html', 'markdown', 'default'] | None` - формат сообщения. `Bot.default_format` по умолчанию

- `notify: bool` - уведомлять ли участников о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - отключить предпросмотр ссылок. `False` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - инлайн-клавиатура. `None` по умолчанию

- `attachments: List[Attachment] | None` - список вложений. `None` по умолчанию

### `Message.reply(text: str, format: Literal['html', 'markdown', 'default'] | None = 'default', notify: bool = True, disable_link_preview: bool = False, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None) -> Message`

Отвечает на это сообщение.

- `text: str` - текст сообщения. Максимум 4000 символов

- `format: Literal['html', 'markdown', 'default'] | None` - формат сообщения. `Bot.default_format` по умолчанию

- `notify: bool` - уведомлять ли участников о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - отключить предпросмотр ссылок. `False` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - инлайн-клавиатура. `None` по умолчанию

- `attachments: List[Attachment] | None` - список вложений. `None` по умолчанию

## `MessageRecipient`

Информация о получателе сообщения. Может быть чатом или пользователем

- `chat_id: int | None` - ID чата

- `chat_type: Literal['chat', 'dialog']` - тип получателя. `chat` - чат, `dialog` - ЛС пользователя

- `user_id: int | None` - ID пользователя, если получатель является пользователем

## `MessageBody`

Информация о содержимом сообщения.

- `message_id: str` - ID сообщения

- `seq: int` - порядковый номер сообщения в чате

- `text: str | None` - текст сообщения. Может быть `None` для вложений

- `attachments: List[Attachment] | None` - список вложений. Может быть `None`

- `markup: List[Markup] | None` - форматирование сообщения. Может быть `None`

## `Markup`

Один токен форматирования сообщения.

- `type: Literal['strong', 'emphasized', 'monospaced', 'link', 'strikethrough', 'underline', user_mention', 'heading', 'highlighted]` - тип форматирования

  - `strong` - **полужирный** текст

  - `emphasized` - *курсивный* текст

  - `monospaced` - `моноширинный` текст

  - `link` - ссылка

  - `strikethrough` - ~~зачеркнутый~~ текст

  - `underline` - подчеркнутый текст

  - `user_mention` - упоминание пользователя

  - `heading` - заголовок

  - `highlighted` - красный текст

- `start: int` - позиция начала токена

- `length: int` - длина токена

- `user_link: str | None` - @username упомянутого пользователя. `None` если `type` не `user_mention`

- `user_id: int | None` - ID упомянутого пользователя. `None` если `type` не `user_mention`

- `url: str | None` - URL ссылки. `None` если `type` не `link`

## `LinkedMessage`

Оригинальное пересланное сообщение или сообщение, на которое ответили.

- `type: str` - тип ссылки. `forward` - пересланное сообщение, `reply` - ответ

- `sender: User` - отправитель оригинального сообщения

- `message: MessageBody` - содержимое оригинального сообщения

- `chat_id: int | None` - ID чата, в котором было оригинальное сообщение. `None` если `type` не `forward`

## `BotStartPayload`

Информация, отправленная функции с декоратором `Bot.on_bot_start`.

Декоратор вызывается при нажатии кнопки "Начать" в ЛС бота пользователем.

- `chat_id: int` - ID чата

- `user: User` - информация о пользователе, который нажал кнопку "Начать"

- `payload: str | None` - дополнительная информация. Может быть `None`

- `user_locale: str | None` - язык пользователя в формате IETF BCP 47. Может быть `None`

## `CommandContext`

Информация, отправленная функции с декоратором `Bot.on_command`.

Декоратор вызывается при вводе команды.

- `message: Message` - сообщениие с введённой командой

- `sender: User` - отправитель сообщения. Является `message.sender`

- `recipient: MessageRecipient` - получатель сообщения. Является `message.recipient`

- `command_name: str` - название команды

- `args: List[str]` - аргументы команды

- `args_raw: str` - сырые, неразделённые пробелами аргументы команды. Полезно, если нужно обрабатывать аргументы команды, которые содержат пробелы

### `CommandContext.send(text: str, format: Literal['html', 'markdown', 'default'] | None = 'default', notify: bool = True, disable_link_preview: bool = False, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None) -> Message`

Отправляет сообщение в чат, в который была отправлена команда.

- `text: str` - текст сообщения. Максимум 4000 символов

- `format: Literal['html', 'markdown', 'default'] | None` - формат сообщения. `Bot.default_format` по умолчанию

- `notify: bool` - уведомлять ли участников о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - отключить предпросмотр ссылок. `False` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - инлайн-клавиатура. `None` по умолчанию

- `attachments: List[Attachment] | None` - список вложений. `None` по умолчанию

### `CommandContext.reply(text: str, format: Literal['html', 'markdown', 'default'] | None = 'default', notify: bool = True, disable_link_preview: bool = False, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None) -> Message`

Отвечает на сообщение с командой.

- `text: str` - текст сообщения. Максимум 4000 символов

- `format: Literal['html', 'markdown', 'default'] | None` - формат сообщения. `Bot.default_format` по умолчанию

- `notify: bool` - уведомлять ли участников о сообщении. `True` по умолчанию

- `disable_link_preview: bool` - отключить предпросмотр ссылок. `False` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - инлайн-клавиатура. `None` по умолчанию

- `attachments: List[Attachment] | None` - список вложений. `None` по умолчанию

## `Callback`

Информация, отправленная функции с декоратором `Bot.on_button_callback`.

Декоратор вызывается при нажатии кнопки типа `CallbackButton`.

- `timestamp: float` - время нажатия кнопки

- `callback_id: str` - ID callback-а

- `user: User` - пользователь, нажавший кнопку

- `payload: str | None` - Payload, указанный при создании `CallbackButton`. Может быть `None`

- `user_locale: str | None` - язык пользователя в формате IETF BCP 47. Может быть `None`

### `answer(notification: "str | None" = None, text: str | None = None, format: Literal['html', 'markdown', 'default'] | None = 'default', notify: bool = True, keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None = None, attachments: List[Attachment] | None = None)`

Отвечает на нажатие кнопки.

Либо `notification`, либо `text`, либо `attachments` должны быть заданы.

Если `keyboard` или `attachments` не заданы, то они не будут изменены.

- `notification: "str | None"` - небольшой попап-уведомление, который увидит пользователь. Может быть `None`

- `text: str | None` - новый текст сообщения, на котором была кнопка. Максимум 4000 символов. Может быть `None`

- `format: Literal['html', 'markdown', 'default'] | None` - формат сообщения. `Bot.default_format` по умолчанию

- `notify: bool` - уведомлять ли участников о изменении сообщения. `True` по умолчанию

- `keyboard: List[List[buttons.Button]] | buttons.KeyboardBuilder | None` - инлайн-клавиатура. `None` по умолчанию

- `attachments: List[Attachment] | None` - список вложений. `None` по умолчанию

## `Image(url: str)`

Изображение.

- `url: str` - ссылка на изображение

## ImageRequestPayload(url: "str | None" = None, token: "str | None" = None)

Изображение, загружаемое для аватарки или иконки чата или профиля.

Либо `url`, либо `token` должны быть заданы. Не может быть задано и `url` и `token`

- `url: str` - ссылка на изображение

- `token: str` - токен изображения, полученный через `Bot.upload_image().payload.token` или с уже загруженного изображения

## `Chat`

Чат.

- `chat_id: int` - ID чата

- `type: str` - тип чата. `dialog` для ЛС или `chat` для группы

- `status: str` - кем бот является в чате.

  - `active` - бот участник чата

  - `removed` - бот был удален из чата

  - `left` - бот покинул чат
  
  - `closed` - чат закрыт

  - `suspended` - бот был остановлен пользователем. Доступно только если `type` - `dialog`.

- `title: str | None` - название чата. Может быть `None` для ЛС

- `description: str | None` - описание чата. Может быть `None`

- `icon: Image | None` - иконка чата. Может быть `None` для ЛС

- `last_event_time: int` - время последнего события в чате

- `participants_count: int` - количество участников в чате. Для ЛС всегда `2`

- `is_public: bool` - является ли чат публичным. Для ЛС всегда `False`

- `owner_id: int | None` - ID владельца чата. Может быть `None` для ЛС

- `participants: Dict[int, int] | None` - словарь с ID участников и их последней активностью в чате. Может содержать пользователей с временем последней активности `0`. Но может быть `None` если запрашивается список чатов

- `link: str | None` - ссылка на чат. Может быть `None` для ЛС

- `messages_count: int | None` - количество сообщений в чате. `None`, если чат не групповой

- `dialog_with_user: User | None` - пользователь, с которым ведется диалог. `None`, если чат не ЛС

- `chat_message_id: str | None` - ID сообщения, содержащего кнопку, через которую был создан чат. Для чатов, созданных через `buttons.ChatButton`

- `pinned_message: Message | None` - сообщение, которое закреплено в чате. Может быть `None` если закреплено ничего или если запрашивается список чатов
