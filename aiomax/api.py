import requests
from . import classes

class Bot:
    def __init__(self, access_token: str):
        '''
        Bot init
        '''
        self.session = requests.Session()
        self.session.params = {
            "access_token": access_token
        }
    
    async def get(self, *args, **kwargs):
        '''
        Sends a GET request to the API.
        '''
        return self.session.get(
            *args,
            **kwargs
        )
    
    async def post(self, *args, **kwargs):
        '''
        Sends a POST request to the API.
        '''
        return self.session.post(
            *args,
            **kwargs
        )

    async def me(self):
        '''
        Returns info about bot
        '''
        request = await self.get(f"https://botapi.max.ru/me")
        return request.json()

    async def patch_me(self, name: str | None = None, description: str | None = None, commands: list[classes.BotCommand] | None = None, photo: classes.PhotoAttachmentRequestPayload = None):
        '''
        Allows you to change information about the current bot. Fill in only those fields that need to be updated. All others will remain unchanged.
        
        :param name: Bot display name
        :param description: Bot description
        :param commands: Commands supported by the bot. To remove all commands, pass an empty list.
        :param photo: Request to set up a bot photo
        '''
        if commands:
            commands = [i.as_dict() for i in commands]   
        if photo:
            photo = photo.as_dict()
        
        vars = {
            "name": name,
            "description": description,
            "commands": commands,
            "photo": photo
            }

        payload = {k: v for k, v in vars.items() if v}

        response = self.session.patch(f"https://botapi.max.ru/me", json=payload)
        return response.json()
    
    async def get_chats(self, count: int | None = None, marker: int | None = None):
        '''
        Returns information about the chats the bot has participated in. The result includes a list of chats and a marker for moving to the next page.

        :param count:  Number of chats requested. 50 by default
        :param marker: Pointer to the next page of data. Defaults to first page
        '''

        vars = {
            "count": count,
            "marker": marker,
            }

        params = {k: v for k, v in vars.items() if v}

        response = await self.get("https://botapi.max.ru/chats", params=params)

        return response.json()
    
    async def get_chat(self, chatId: int):
        response = await self.get("https://botapi.max.ru/chats", params={"chatId": chatId})

        return response.json()

    async def patch_chat(self, chatId: int, icon: classes.PhotoAttachmentRequestPayload | None = None, title: str | None = None, pin: str | None = None, notify: bool | None = None):
        '''
        Allows you to edit chat information, including the name, icon and pinned message.

        :param chatId: chat Id
        :param icon: Image attachment request
        :param title: Chat name. From 1 to 200 characters
        :param pin: Id of the message to be pinned in the chat room
        :param notify: If default, participants will receive a system notification of the change
        '''

        vars = {
            "icon": icon,
            "title": title,
            "pin": pin,
            "notify": notify
            }
        
        payload = {k: v for k, v in vars.items() if v}

        response = self.session.patch(f"https://botapi.max.ru/chats/{chatId}", json=payload)
        return response.json()
    
    async def post_action(self, chatId: int, action: str):
        '''
        Allows you to send bot actions to chat, such as 'typing' or 'sending a photo'.
        :param chatId: Chat Id
        :param action: Constant from aiomax.types.Actions
        '''

        response = await self.post(f"https://botapi.max.ru/chats/{chatId}/actions", json={"action": action})

        return response.json()