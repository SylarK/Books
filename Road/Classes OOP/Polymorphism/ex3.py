#   Polimorfismo com o conceito de herança
#   Esta é a maneira com que mais utilizamos o polimorfismo

class Animal():
    def __init__(self, name, age, typeAnimal):
        self.name         = name
        self.age          = age
        self.typeAnimal   = typeAnimal

    def info(self):
        print('Name : ' + self.name)
        print('Age  : ' + str(self.age))    #Lembrando que precisamos realizar a conversão do int para string para concatenar
        print('Type : ' + self.typeAnimal)

    def walk(self):
        print('The animal is walking')

class Dog(Animal):

    def sounds():
        print('Au au')

class Bird(Animal):

    def walk(self):
        print('The bird can fly. The bird is flying!!')

myDog  = Dog('Rex', 2, 'Dog')
myBird = Bird('Prince', 1, 'Bird')

for animal in (myDog, myBird):
    animal.info()
    animal.walk()
    print('-'*30)