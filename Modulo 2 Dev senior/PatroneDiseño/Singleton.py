def singleton(cls):
    instances = {}
    
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrapper

@singleton
class Event_Register:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

obj1 = Event_Register("admin", 1234)
obj2 = Event_Register("admin", 0000)
        
print(obj1 is obj2)