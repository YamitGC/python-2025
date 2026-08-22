from abc import ABC, abstractmethod

class Personaje(ABC): 
    
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
        
    def pocion_vida(self, pocion):
        
        if self.vida > 0:
            if pocion > 0:
                self.pocion -= 1
                self.vida += 10
                print(f'{self.nombre} ha recuperado 10 de vida. Tiene {self.pocion} pociones de vida restantes.')
            else:
                print(f'{self.nombre} no tiene pociones de vida, por lo que no puede recuperar vida.')
        else:
            print('El personaje no esta vivo')
        
    def subir_nivel(self):
        
        if self.vida > 0:
            self.nivel += 1
            print(f'{self.nombre} ha subido al nivel {self.nivel}')
            self.daño += 1
            self.vida += 10
            self.def_fisica += 1
            self.def_magica += 1
            self.pocion += 1
        else:
            print('El personaje no se encuentra con vida')
        
    @abstractmethod
    def atacar(self, enemigo):
        pass
    
    def duelo_a_muerte(self, enemigo):
        while self.esta_vivo() and enemigo.esta_vivo():
            self.atacar(enemigo)
            print(f'Vida de {enemigo.nombre}: {enemigo.vida}')
            if not enemigo.esta_vivo(): # A partir de aqui modificacion para evitar vida negativa del perdedor
                if enemigo.vida <= 0:
                    enemigo.vida = 0
                    break
                elif self.vida <= 0:
                    self.vida = 0
                    break
            enemigo.atacar(self)
            print(f'Vida de {self.nombre}: {self.vida}')
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        print(f'\n{ganador.nombre} ha ganado la batalla!')
        print(f'Resumen de la batalla: {ganador.nombre} derrotó a {perdedor.nombre} en un duelo épico.')
        print(f'Vida final: {ganador.nombre} ({ganador.vida}) vs {perdedor.nombre} ({perdedor.vida})')
        
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
    
    """
    Personaje tipo mago. Su daño es incrementado por 1.5 gracias a su magia.
    """
    
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
        
# Nombre, daño, vida, defensa fisica, defensa magica.

guerrero1 = Guerrero('Hercules', 8, 50, 9, 7, 'Espada de Hierro')
#print(guerrero1)

guerrero2 = Guerrero('Dave', 9, 50, 7, 5, 'Espada de Oro') 
#print(guerrero2)

mago1 = Mago('Gandalf', 10, 50, 5, 10, 'Fuego')
#print(mago1)

print(guerrero1.atacar(guerrero2))
#print(guerrero2.atacar(guerrero1))

#print(guerrero1.atacar(mago1))

guerrero1.duelo_a_muerte(guerrero2)
guerrero2.subir_nivel()
guerrero2.pocion_vida(1)
print(guerrero2)