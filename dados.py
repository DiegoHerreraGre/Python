import random

class DadoUno:
    
    def __init__(self, numeros_de_lados, veces_que_se_lanza, cantidad_de_dados):
        self.numeros_de_lados = numeros_de_lados
        self.veces_que_se_lanza = veces_que_se_lanza
        self.cantidad_de_dados = cantidad_de_dados
        
    def lanzar_dado(self):
        print(f"Lanzando dado de {self.numeros_de_lados} lados")
        return random.randint(1, self.numeros_de_lados)
    
    def lanzar_dados(self):
        suma = 0
        print(f"Lanzando {self.cantidad_de_dados} dados de {self.numeros_de_lados} lados")
        for i in range(self.veces_que_se_lanza):
            for j in range(self.cantidad_de_dados):
                suma += self.lanzar_dado()
        print(f"La suma de los dados es: {suma}")
        return suma
    
    def lanzar_dados_con_suma(self):
        print(f"Lanzando {self.cantidad_de_dados} dados de {self.numeros_de_lados} lados")
        suma = 0
        for i in range(self.veces_que_se_lanza):
            for j in range(self.cantidad_de_dados):
                suma += self.lanzar_dado()
        print(f"La suma de los dados es: {suma}")
        return suma
    
dado = DadoUno(6, 1, 1)
dado.lanzar_dados()