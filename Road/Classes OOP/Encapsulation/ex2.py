#   Classe carro terá dois métodos : 
#   drive() e updateSoftware()
#   Quando a classe for criada, ela chamará o método privado updateSoftware()
#   O método não poderá ser chamado diretamente pelo objeto, apenas de dentro do objeto.

class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('Driving arround the city')

    def __updateSoftware(self):
        print('We are searching for a new update ! ')
        print('The update has been completed.')
    
bluecar = Car()
bluecar.drive()