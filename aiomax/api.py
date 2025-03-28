import requests

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
    
    async def patch_me(self, **kwargs):
        '''
        Allows you to change information about the current bot. Fill in only those fields that need to be updated. All others will remain unchanged.
        :param name: Bot display name
        :param description: Bot description
        '''
        response = self.session.patch(f"https://botapi.max.ru/me", json=kwargs)
        return response.json()