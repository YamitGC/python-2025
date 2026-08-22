from abc import ABC, abstractmethod
from os import system

class Personaje(ABC): 
    
    nivel = 1
    pocion = 0
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica):
        self.nombre = nombre
        self.daño = daño
        self.vida = vida
        self.def_fisica = def_fisica
        self.def_magica = def_magica
        
    @abstractmethod
    def __str__(self):
        pass 
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto')
        
    def pocion_vida(self):
        
        if self.esta_vivo:
            if self.pocion > 0:
                self.vida += 25
                self.pocion -= 1
                print(f'{self.nombre} ha recuperado 25 de vida. Tiene {self.pocion} pociones de vida restantes.')
            else:
                print(f'{self.nombre} no tiene pociones de vida, por lo que no puede recuperar vida.')
        else:
            print('El personaje no esta vivo')
        
    def subir_nivel(self):
        
        if self.esta_vivo:
            self.nivel += 1     
            self.daño += 1
            self.vida += 10
            self.def_fisica += 1
            self.def_magica += 1
            self.pocion += 1
            print(f'{self.nombre} ha subido al nivel {self.nivel}')
        else:
            print('El personaje no se encuentra con vida')
        
    @abstractmethod
    def atacar(self, enemigo):
        pass
    
    def duelo_a_muerte(self, enemigo):
        while self.esta_vivo() and enemigo.esta_vivo():
            self.atacar(enemigo)
            if not enemigo.esta_vivo(): 
                break    
            enemigo.atacar(self)
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        perdedor.morir()
        print(f'{ganador.nombre} ha ganado la batalla  🎉')
        print(f'Vida final: 👑 {ganador.nombre} (❤️  {ganador.vida}) vs 💀 {perdedor.nombre} (❤️  {perdedor.vida})\n')
        
class Guerrero(Personaje):
    
    """
    Personaje tipo Guerrero. Su daño fisico es incrementado x2 gracias a su espada
    """
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, espada):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.espada = espada
    
    def __str__(self):
        return f'{self.nombre} 🤺  nivel {self.nivel} | 🗡️  {self.daño} | ❤️  {self.vida} | 🛡️  Fisica: {self.def_fisica} | 🛡️  Magica: {self.def_magica} | -Espada: {self.espada}\n'
        
    def atacar(self, enemigo):
        daño_realizado = self.daño * 2 - enemigo.def_fisica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            enemigo.vida -= daño_realizado
            print(f'{self.nombre} ⚔️  {enemigo.nombre} causandole {daño_realizado} de daño fisico | ❤️  Vida restante de {enemigo.nombre}: {enemigo.vida}\n')
            
class Mago(Personaje):
    
    """
    Personaje tipo mago. Su daño es incrementado por 1.5 gracias a su magia.
    """
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, magia):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.magia = magia
        
    def __str__(self):
        return f'{self.nombre} 🧙  nivel {self.nivel} | ☄️  {self.daño} | ❤️  {self.vida} | 🛡️  fisica: {self.def_fisica} | 🛡️  magica: {self.def_magica} | -Magia: {self.magia} \n'
          
    def atacar(self, enemigo):
        daño_realizado = self.daño * 1.5 - enemigo.def_magica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            enemigo.vida -= daño_realizado
            print(f'{self.nombre} ⚔️  {enemigo.nombre} causandole {daño_realizado} de daño magico | ❤️  Vida restante de {enemigo.nombre}: {enemigo.vida}\n')  

class FabricaPersonajes:
    
    @staticmethod
    def crear_personaje(tipo, nombre, daño, vida, def_fisica, def_magica, tipo_arma):
        if tipo == "guerrero":
            return Guerrero(nombre, daño, vida, def_fisica, def_magica, tipo_arma)
        elif tipo == "mago":
            return Mago(nombre, daño, vida, def_fisica, def_magica, tipo_arma)
        else:
            raise ValueError("Tipo de personaje no válido")
    
def inputs_personaje():
    
    tipo_arma = ''
    
    while True:
        tipo = input('Digite el tipo de personaje (guerrero/mago): ')
        if tipo != 'guerrero' and tipo != 'mago':
            limpiar_pantalla()
            print('\nERROR. Tipo de personaje incorrecto\n')
            continue
        nombre_personaje = input('Nombre del personaje: ')
        daño = int(input('Daño del personaje: '))
        vida = int(input('Vida del personaje: '))
        defensa_fisica = int(input('Defensa fisica del personaje: '))
        defensa_magica = int(input('Defensa magica del personaje: '))
        if tipo == 'guerrero':
            tipo_arma = input('Digite la espada del personaje: ')
        elif tipo == 'mago':
            tipo_arma = input('Digite la magia del personaje: ')
    
        return tipo, nombre_personaje, daño, vida, defensa_fisica, defensa_magica, tipo_arma

"""def crear_guerrero():
    
    atributos = inputs_personaje()
    espada = input('¿Cuál espada desea?: ')
    
    return Guerrero(*atributos, espada)

def crear_mago():
    atributos = inputs_personaje()
    magia = input('¿Cuál magia desea?: \n')
    return Mago(*atributos, magia)"""
    
def limpiar_pantalla():
    
    system('clear')
    
def listar_personajes(personajes):
    
    for personaje in personajes:
        print(f'''{personajes.index(personaje)+1}. {personaje}''')
        
def partida():
    
    guerrero1 = Guerrero('Hercules', 10, 50, 11, 10, 'Oro')
    guerrero2 = Guerrero('Dave', 9, 50, 9, 6, 'Hierro')
    guerrero3 = Guerrero('Ragnar', 13, 50, 11, 6, 'Diamante')
    mago1 = Mago('Lucas', 12, 50, 7, 11, 'Hielo')
    personajes = [guerrero1, guerrero2, guerrero3, mago1]
    
    while True:
        
        print('1. Personaje nuevo')
        print('2. Duelo a muerte')
        print('3. Listado de personajes')
        print('4. Subir de nivel')
        print('5. Recuperar vida')
        print('6. Salir')
        
        opcion = int(input('\nElija una opcion (1-6): '))
        
        if opcion > 0 and opcion < 7:
            if opcion == 1:
                limpiar_pantalla()
                #guerrero = crear_guerrero()
                atributos = inputs_personaje()
                personaje = FabricaPersonajes.crear_personaje(*atributos)
                personajes.append(personaje)
                limpiar_pantalla()
            
            elif opcion == 2:
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
            
            elif opcion == 3:
                limpiar_pantalla()
                if len(personajes) == 0:
                    limpiar_pantalla()
                    print('No hay personajes para mostrar\n')
                    continue
                listar_personajes(personajes) 
            
            elif opcion == 4:
                limpiar_pantalla()
                if len(personajes) == 0:
                    limpiar_pantalla()
                    print('No hay personajes para subir de nivel\n')
                    continue
                print('¿Cual personaje desea subir de nivel?: ')
                listar_personajes(personajes)
                personaje = personajes[int(input('Personaje: '))-1]
                personaje.subir_nivel()
            
            # En otras palabras, el -1 se utiliza para convertir el índice "humano" (que comienza en 1) a un índice "de lista" (que comienza en 0).
            
            elif opcion == 5:
                limpiar_pantalla()
                if len(personajes) == 0:
                    limpiar_pantalla()
                    print('No hay personajes para recuperar vida\n')
                    continue
                else:
                    print('¿Cual personaje desea recuperar vida?: ')
                    listar_personajes(personajes)
                    personaje = personajes[int(input('Personaje: '))-1]
                    personaje.pocion_vida()
            
            elif opcion == 6:
                print('Gracias por jugar !')
                break
        
        else:
            limpiar_pantalla()
            print('ERROR.Ingrese una opcion valida\n')
            
partida()