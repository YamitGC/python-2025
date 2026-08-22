class Singleton:
    
    _instancia = None
    
    @staticmethod
    def obtener_instancia():
        if Singleton._instancia is None:
            Singleton._instancia = Singleton()
        return Singleton._instancia
    
    def __init__(self):
        pass
    
obj1 = Singleton.obtener_instancia()
obj2 = Singleton.obtener_instancia()

print(obj1 is obj2)