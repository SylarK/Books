#   Inheritance
#   Permite que possamos definir uma classe que terá como herança todos os métodos e atributos de outra
#   classe (parent class). 

#   Create a Parent Class

class Person :
    #constructor
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    #method
    def printname(self):
        print('Name: ' + self.firstName, self.lastName)

print('-'*30)
print('class Parent')

person1 = Person('Harry', 'Potter')
person1.printname()

print('-'*30)
print('class Child')

#   Create a Child

class Client(Person):
    pass
    cpf = ''

    def getcpf(self, number):
        self.cpf = number

    def alldata(self):
        self.printname()
        print('Cpf: ' + self.cpf)

cliente = Client('Ron', 'Weasley')
cliente.getcpf('700.025.269-59')
cliente.alldata()

#   SUPER function - Faz com que a classe child herde todos os métodos e propriedades.
#class Student(Person):
#  def __init__(self, fname, lname, year):
#    super().__init__(fname, lname)
#    self.graduationyear = year

#   def welcome(self):
#       print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)