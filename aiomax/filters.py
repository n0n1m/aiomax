from . import classes

import re

class startswith:
    def __init__(self, prefix: str):
        '''
        :param prefix: Prefix to check
        
        Checks if the message starts with the given prefix
        '''
        self.prefix = prefix
    
    def __call__(self, obj: "classes.Message | classes.Callback"):
        if hasattr(obj, "content"):
            return obj.content.startswith(self.prefix)
        else:
            raise Exception(f"Class {type(object).__name__} has no content")

class regex:
    def __init__(self, pattern: str):
        '''
        :param pattern: Regex pattern to check
        
        Checks if the message matches the given pattern
        '''
        self.pattern = pattern
    
    def __call__(self, obj: "classes.Message | classes.Callback"):
        if hasattr(obj, "content"):
            return re.fullmatch(self.pattern, obj.body.text)
        else:
            raise Exception(f"Class {type(obj).__name__} has no content")