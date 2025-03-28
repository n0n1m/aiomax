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

    async def me(self):
        '''
        Returns info about bot
        '''
        info = await self.get(f"https://botapi.max.ru/me")
        return info.json()

    async def patch_me(self, name: str = None, description: str = None, commands: list[classes.BotCommand] = None, photo: classes.PhotoAttachmentRequestPayload = None):
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