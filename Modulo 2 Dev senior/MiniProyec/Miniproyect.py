from abc import ABC, abstractmethod

class Personaje(ABC):
    
    nivel = 1
    posion = 0
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica ):
        self.nombre = nombre
        self.daño = daño
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
        print(f"{self.nombre} Ha muerto")
        
    def posion_vida(self, pocion):
        
        if self.vida > 0:
            if self.posion > 0:
                self.posion -= 1
                self.vida += 10
                print(f"{self.nombre} ha recuperado 10 de vida. Le quedan {self.posion}")
            else:
                print(f"{self.nombre} no tiene posiones de vida")
        else:
            print("El jugador está muerto")    
            
    def subir_nivel(self):
        
        if self.vida > 0:
            self.nivel += 1
            print(f"{self.nombre} ha subido de nivel {self.nivel}")
            self.daño += 1
            self.vida += 10
            self.def_fisica += 1
            self.def_magica += 1
            self.posion += 1
        else:
            print("El jugador está muerto")
            
    @abstractmethod
    
    def atacar(self,enemigo):
        pass
    
    def duelo_a_muerte(self,enemigo):
        while self.esta_vivo() and enemigo.esta_vivo():
            self.atacar(enemigo)
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
            if not enemigo.esta.vivo():
                if enemigo.vida <= 0:
                    enemigo.vida = 0
                    break
                elif self.vida <= 0:
                    self.vida = 0
                    break
            enemigo.atacar(self)
            print(f"vida de {self.nombre}: {self.vida}")
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        print(f"\n {ganador.nombre} has ganado la batalla")
        print(f"Resumen de la batalla: {ganador.nombre} derroto a {perdedor.nombre} en un duelo epico. ")
        print(f"Vida final: {ganador.nombre} tiene {ganador.vida} vs {perdedor.nombre} con {perdedor.vida}")
        
class Gerrero(Personaje):
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, espada):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.espada = espada
        
    def _str_(self):
        return f"atributos de {self.nombre} son:\n Vida: {self.vida} \n Daño: {self.daño} \n Def fisica: {self.def_fisica} \n Def magica: {self.def_magica} \n Espada: {self.espada}"
    
    def atacar(self, enemigo):
        return super().atacar(enemigo)
                
                
            
           
            
        
        