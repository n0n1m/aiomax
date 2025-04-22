from . import classes

import re

class startswith:
    def __init__(self, prefix: str):
        self.prefix = prefix
    
    def __call__(self, obj: "classes.Message | classes.Callback"):
        if hasattr(obj, "content"):
            return obj.content.startswith(self.prefix)
        else:
            raise Exception(f"Class {type(object).__name__} has no content")

class regex:
    def __init__(self, pattern: str):
        self.pattern = pattern
    
    def __call__(self, obj: "classes.Message | classes.Callback"):
        if hasattr(obj, "content"):
            return re.fullmatch(self.pattern, obj.body.text)
        else:
            raise Exception(f"Class {type(obj).__name__} has no content")