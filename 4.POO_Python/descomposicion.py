class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = color
        self.marca = marca
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def set_motor(self, motor):
        self._motor = motor
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'

class Motor:

    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        pass

if __name__ == '__main__':

    # Inicializamos un motor con 10 cilintros
    motorFerrari = Motor(10)

    # Creamos automovil
    ferrari = Automovil('Ferarri 2020','Ferrari','Negro')
    print("MARCA: "+ferrari.marca)
    print("CILINDROS: " + str(ferrari.motor.cilindros))

    # Cambiamos el motor
    ferrari.set_motor = motorFerrari
    print("MARCA: "+ferrari.marca)
    print("CILINDROS: " + str(ferrari.motor.cilindros))
