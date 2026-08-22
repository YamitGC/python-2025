from abc import ABC, abstractmethod
from os import system

class Personaje(ABC): 
    
    nivel = 1
    pocion = 1
    
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
    
    def morir(self, personajes):
        self.vida = 0
        print(f'{self.nombre} ha muerto')
        personajes.remove(self)
        
    def pocion_vida(self):
        
        if self.vida > 0:
            if self.pocion > 0:
                self.vida += 25
                self.pocion -= 1
                print(f'{self.nombre} ha recuperado 25 ❤️ . Tiene {self.pocion} pociones de vida restantes.\n')
            else:
                print(f'❌  {self.nombre} no tiene pociones de vida.\n')
        else:
            print('\nEl personaje no esta vivo 💀 \n')
        
    def subir_nivel(self):
        
        if self.vida > 0:
            self.nivel += 1     
            self.daño += 1
            self.vida += 10
            self.def_fisica += 1
            self.def_magica += 1
            self.pocion += 1
            print(f'{self.nombre} ha subido al nivel {self.nivel}  🆙 ✔️\n')
        else:
            print('\nEl personaje no esta vivo 💀 \n')
        
    @abstractmethod
    def atacar(self, enemigo):
        pass
    
    def duelo_a_muerte(self, enemigo, personajes):
        
        while self.esta_vivo() and enemigo.esta_vivo():
            self.atacar(enemigo)
            if not enemigo.esta_vivo(): 
                break    
            enemigo.atacar(self)
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        perdedor.morir(personajes)
        print(f'{ganador.nombre} ha ganado la batalla  🎉')
        print(f'Vida final: 👑 {ganador.nombre} (❤️  {ganador.vida}) vs 💀 {perdedor.nombre} (❤️  {perdedor.vida})\n')
        ganador.subir_nivel()
        
def inputs_personaje():
    
    tipo_arma = ''
    
    while True:
        try:
            tipo = input('Digite el tipo de personaje (guerrero/mago): ')
            if tipo != 'guerrero' and tipo != 'mago':
                limpiar_pantalla()
                raise ValueError("\nError. Tipo de personaje incorrecto\n")
            #print('\nERROR. Tipo de personaje incorrecto\n')
            #continue
            nombre_personaje = input('Nombre del personaje: ').strip()
            if nombre_personaje.isalnum() or not nombre_personaje:
                raise ValueError("El nombre no debe estar vacio ni con numeros.")
            
            daño = int(input('Daño del personaje: '))
            vida = int(input('Vida del personaje: '))
            defensa_fisica = int(input('Defensa fisica del personaje: '))
            defensa_magica = int(input('Defensa magica del personaje: '))
            if tipo == 'guerrero':
                tipo_arma = input('Digite la espada del personaje: ')
            elif tipo == 'mago':
                tipo_arma = input('Digite la magia del personaje: ')
    
            return tipo, nombre_personaje, daño, vida, defensa_fisica, defensa_magica, tipo_arma
    
        except ValueError as e:
            limpiar_pantalla()
        print(f"Error. Datos incorrectos")
        return
        
        
def limpiar_pantalla():
    
    system('clear')
    
def listar_personajes(personajes):
    
    for personaje in personajes:
        print(f'''{personajes.index(personaje)+1}. {personaje}''')
            
def valida_personajes(lista_personajes = list):
    
    if len(lista_personajes) < 2:
        limpiar_pantalla()
        print('ERROR. No hay suficientes personajes para hacer eso. \n')
        return False
        