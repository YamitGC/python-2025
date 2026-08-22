from abc import ABC, abstractmethod
from os import system

class Personaje(ABC): 
    
    nivel = 1
    pocion = 0
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica):
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
            if not enemigo.esta_vivo(): 
                if enemigo.esta_vivo:
                    enemigo.vida = 0
                    break
                elif self.esta_vivo:
                    self.vida = 0
                    break
            enemigo.atacar(self)
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        print(f'{ganador.nombre} ha ganado la batalla!')
        print(f'Vida final: {ganador.nombre} ({ganador.vida}) vs {perdedor.nombre} ({perdedor.vida})\n')
        
class Guerrero(Personaje):
    
    """
    Personaje tipo Guerrero. Su daño fisico es incrementado x2 gracias a su espada
    """
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, espada):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.espada = espada
    
    def _str_(self):
        return f'{self.nombre} 🤺  nivel {self.nivel} | 🗡  {self.daño} | ❤  {self.vida} | 🛡  Fisica: {self.def_fisica} | 🛡  Magica: {self.def_magica} | -Espada: {self.espada}\n'
        
    def atacar(self, enemigo):
        daño_realizado = self.daño * 2 - enemigo.def_fisica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            enemigo.vida -= daño_realizado
            print(f'{self.nombre} ⚔  {enemigo.nombre} causandole {daño_realizado} de daño fisico | ❤  Vida restante de {enemigo.nombre}: {enemigo.vida}\n')
            
class Mago(Personaje):
    
    """
    Personaje tipo mago. Su daño es incrementado por 1.5 gracias a su magia.
    """
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, magia):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.magia = magia
        
    def _str_(self):
        return f'{self.nombre} 🧙  nivel {self.nivel} | ☄  {self.daño} | ❤  {self.vida} | 🛡  fisica: {self.def_fisica} | 🛡  magica: {self.def_magica} | -Magia: {self.magia} \n'
          
    def atacar(self, enemigo):
        daño_realizado = self.daño * 1.5 - enemigo.def_magica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            enemigo.vida -= daño_realizado
            print(f'{self.nombre} ⚔  {enemigo.nombre} causandole {daño_realizado} de daño magico | ❤  Vida restante de {enemigo.nombre}: {enemigo.vida}\n')  

def inputs_personaje():
    
    nombre_personaje = input('Nombre del personaje: ')
    daño = int(input('Daño del personaje: '))
    vida = int(input('Vida del personaje: '))
    defensa_fisica = int(input('Defensa fisica del personaje: '))
    defensa_magica = int(input('Defensa magica del personaje: '))
    
    return nombre_personaje, daño, vida, defensa_fisica, defensa_magica

def crear_guerrero():
    
    atributos = inputs_personaje()
    espada = input('¿Cuál espada desea?: ')
    
    return Guerrero(*atributos, espada)

def crear_mago():
    atributos = inputs_personaje()
    magia = input('¿Cuál magia desea?: \n')
    return Mago(*atributos, magia)

def limpiar_pantalla():
    system("cls")
    
def listar_personajes(personajes):
    
    for personaje in personajes:
        print(f'''{personajes.index(personaje)+1}. {personaje}''')
        
def partida():
    
    """guerrero1 = Guerrero('Hercules', 10, 50, 11, 10, 'Oro')
    guerrero2 = Guerrero('Dave', 9, 50, 9, 6, 'Hierro')
    mago1 = Mago('Lucas', 12, 50, 7, 11, 'Hielo')"""
    personajes = []
    
    # guerrero1, guerrero2, mago1
    
    while True:
        
        print('1. Guerrero')
        print('2. Mago')
        print('3. Duelo a muerte')
        print('4. Listado de personajes')
        print('5. Subir de nivel')
        print('6. Recuperar vida')
        print('7. Salir')
        
        opcion = int(input('\nElija una opcion (1-7): '))
        
        if opcion > 0 and opcion < 8:
            if opcion == 1:
                limpiar_pantalla()
                guerrero = crear_guerrero()
                personajes.append(guerrero)
                limpiar_pantalla()
            
            elif opcion == 2:
                limpiar_pantalla()
                mago = crear_mago()
                personajes.append(mago)
                limpiar_pantalla()
            
            elif opcion == 3:
                limpiar_pantalla()
                if len(personajes) < 2:
                    limpiar_pantalla()
                    print('No hay suficientes personajes para un duelo a muerte\n')
                    continue
                else:
                    print('Escoja sus luchadores:')
                    listar_personajes(personajes)
                    personaje1 = personajes[int(input('Personaje 1: '))-1]
                    personaje2 = personajes[int(input('Personaje 2: '))-1]
                    personaje1.duelo_a_muerte(personaje2)
            
            elif opcion == 4:
                limpiar_pantalla()
                if len(personajes) == 0:
                    limpiar_pantalla()
                    print('No hay personajes para mostrar\n')
                    continue
                listar_personajes(personajes) 
            
            elif opcion == 5:
                
                if len(personajes) == 0:
                    limpiar_pantalla()
                    print('No hay personajes para subir de nivel\n')
                    continue
                print('¿Cual personaje desea subir de nivel?: ')
                listar_personajes(personajes)
                personaje = personajes[int(input('Personaje: '))-1]
                personaje.subir_nivel()
            
            # En otras palabras, el -1 se utiliza para convertir el índice "humano" (que comienza en 1) a un índice "de lista" (que comienza en 0).
            
            elif opcion == 6:
                
                if len(personajes) == 0:
                    limpiar_pantalla()
                    print('No hay personajes para recuperar vida\n')
                    continue
                elif personaje.pociones == 0:
                    limpiar_pantalla()
                    print('No tienes pociones de vida\n')
                    continue
                print('¿Cual personaje desea recuperar vida?: ')
                listar_personajes(personajes)
                personaje = personajes[int(input('Personaje: '))-1]
                personaje.pocion_vida(1)
                print(f'{personaje.nombre} ha recuperado {personaje.vida} de vida')
            
            elif opcion == 7:
                print('Gracias por jugar !')
                break
        
        else:
            limpiar_pantalla()
            print('ERROR.Ingrese una opcion valida\n')
    
partida()