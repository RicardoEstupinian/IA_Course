class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Ando caminando')
    
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('Ando pedaleando')


def main():
    persona1 = Persona('Chipi')
    persona2 = Ciclista('Ricardo')
    persona1.avanza()
    persona2.avanza()

if __name__ == '__main__':
    main()