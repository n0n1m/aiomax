from .types import *
from typing import *
from . import buttons


def get_message_body(
    text: str,
    format: "Literal['markdown', 'html'] | None" = None,
    reply_to: "int | None" = None,
    notify: bool = True,
    keyboard: "List[List[buttons.Button]] | None" = None,
) -> dict:
    '''
    Returns the body of the message as json.
    '''
    body = {
        "text": text,
        "format": format,
        "notify": notify
    }

    # replying
    if reply_to:
        body['link'] = {
            "type": 'reply',
            "mid": reply_to
        }

    # keyboard
    if keyboard:
        if isinstance(keyboard, buttons.KeyboardBuilder):
            keyboard = keyboard.to_list()
        body['attachments'] = [{
            'type': 'inline_keyboard',
            'payload': {'buttons': keyboard}
        }]

    return body