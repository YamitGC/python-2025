class Personaje(ABC): #Debe definir al menos un metodo abstracto para que no sea permitido crear un objeto de esta clase
    
    nivel = 1
    pocion = 0
    
    def _init_(self, nombre, daño, vida, def_fisica, def_magica):
        self.nombre = nombre
        self.daño = daño
        self.vida = vida
        self.def_fisica = def_fisica
        self.def_magica = def_magica
        
    @abstractmethod
    def _str_(self):
        pass 
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto')
        
    def pocion_vida(self, pocion_vida):
        if pocion_vida > 0:
            self.pocion_vida -= 1
            self.vida += 10
            print(f'{self.nombre} ha recuperado 10 de vida. Tiene {self.pocion_vida} pociones de vida restantes.')
        else:
            print(f'{self.nombre} no tiene pociones de vida, por lo que no puede recuperar vida.')
        
    def subir_nivel(self):
        self.nivel += 1
        print(f'{self.nombre} ha subido al nivel {self.nivel}')
        self.daño += 1
        self.vida += 10
        self.defensa += 1
        self.pocion_vida += 1
        
    @abstractmethod
    def atacar(self, enemigo):
        pass
    
    def duelo_a_muerte(self, enemigo):
        while self.esta_vivo() and enemigo.esta_vivo():
            self.atacar(enemigo)
            print(f'Vida de {enemigo.nombre}: {enemigo.vida}')
            if not enemigo.esta_vivo():
                break
            enemigo.atacar(self)
            print(f'Vida de {self.nombre}: {self.vida}')
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        print(f'\n{ganador.nombre} ha ganado la batalla!')
        print(f'Resumen de la batalla: {ganador.nombre} derrotó a {perdedor.nombre} en un duelo épico.')
        print(f'Vida final: {ganador.nombre} ({ganador.vida}) vs {perdedor.nombre} ({perdedor.vida})')
        
"""def duelo_a_muerte(self, enemigo):
        while self.esta_vivo() and enemigo.esta_vivo():
            self.ataque_a_muerte(enemigo)
            if not enemigo.esta_vivo():
                break
            enemigo.ataque_a_muerte(self)
            if not self.esta_vivo():
                break
        if self.esta_vivo():
            print(f'{self.nombre} ha ganado la batalla!')
            print(f'Resumen de la batalla: {self.nombre} derrotó a {enemigo.nombre} en un duelo épico.')
            print(f'Vida final: {self.nombre} ({self.vida}) vs {enemigo.nombre} ({enemigo.vida})')
        else:
            print(f'{enemigo.nombre} ha ganado la batalla!')
            print(f'Resumen de la batalla: {enemigo.nombre} derrotó a {self.nombre} en un duelo épico.')
            print(f'Vida final: {self.nombre} ({self.vida}) vs {enemigo.nombre} ({enemigo.vida})')"""
            
    
class Guerrero(Personaje):
    
    """
    Personaje tipo Guerrero. Su daño fisico es incrementado x2 gracias a su espada
    """
    
    def _init_(self, nombre, daño, vida, def_fisica, def_magica, espada):
        super()._init_(nombre, daño, vida, def_fisica, def_magica)
        self.espada = espada
    
    def _str_(self):
        return f'Atributos de {self.nombre} nivel {self.nivel}: Daño: {self.daño} | -Vida: {self.vida} | -Def fisica: {self.def_fisica} | -Defensa magica: {self.def_magica} | -Espada: {self.espada}\n'
        
    def atacar(self, enemigo):
        daño_realizado = self.daño * 2 - enemigo.def_fisica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            print(f'{self.nombre} ataca a {enemigo.nombre} causandole {daño_realizado} de daño fisico.')
            enemigo.vida -= daño_realizado
            return f'{enemigo.nombre} queda con {enemigo.vida} de vida\n'

    
class Mago(Personaje):
    
    def _init_(self, nombre, daño, vida, def_fisica, def_magica, magia):
        super()._init_(nombre, daño, vida, def_fisica, def_magica)
        self.magia = magia
        
    def _str_(self):
        return f'Atributos de {self.nombre} nivel {self.nivel}: Daño: {self.daño} | -Vida: {self.vida} | -Defensa fisica: {self.def_fisica} | -Defensa magica: {self.def_magica} | -Magia de: {self.magia}\n'
          
    def atacar(self, enemigo):
        daño_realizado = self.daño * 1.5 - enemigo.def_magica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            print(f'{self.nombre} ataca a {enemigo.nombre} causandole {daño_realizado} de daño magico.')
            enemigo.vida -= daño_realizado
            return f'{enemigo.nombre} queda con {enemigo.vida} de vida\n'
        
#personaje1 = Personaje('Bukker', 5, 100, 5, 5) # No se puede instanciar a una clase abstracta Personaje


# Nombre, daño, vida, defensa fisica, defensa magica.

guerrero1 = Guerrero('Hercules', 8, 50, 9, 7, 'Espada de Hierro')
#print(guerrero1)

guerrero2 = Guerrero('Dave', 9, 50, 7, 5, 'Espada de Oro') 
#print(guerrero2)

mago1 = Mago('Gandalf', 10, 50, 5, 10, 'Fuego')
#print(mago1)

"""print(guerrero1.atacar(guerrero2))
print(guerrero2.atacar(guerrero1))

print(guerrero1.atacar(mago1))"""


#guerrero1.duelo_a_muerte(guerrero2)