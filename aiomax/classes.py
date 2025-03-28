class BotCommand:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def as_dict(self):
        return {"name": self.name, "description": self.description}
    

class PhotoAttachmentRequestPayload:
    def __init__(self, url: "str | None"):
        self.url = url
    
    def as_dict(self):
        return {"url": self.url}