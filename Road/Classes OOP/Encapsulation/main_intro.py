#   Encapsulation   
#   Um conceito amplamente utilizado na POO.
#   Vem da ideia de "esconder" a um dado ou método de determinada classe. Fazendo com que ela não seja acessada diretamente.
#   Desta forma, previne-se a modificação acidental ou maliciosa de um dado atributo por exemplo.   
#   Protected members (C++ e Java) são membros de classe que não podem ser acessadas fora dela, mas podem ser acessada pelas classes e subclasses.
#   Em Python, por convenção nos referimos a ela com um underscore.

class Primaria():
    def __init__(self):
        self._value = 10

class Secundaria(Primaria):
    def __init__(self):

        # Chamando o construtor da classe Primária.
        Primaria.__init__(self)
        print('Calling class Primaria')
        print(self._value)

#obj_sec = Secundaria()
#obj_pri = Primaria()

#print(obj_pri.value)

#   Private Members
#   Em Python para declaramos uma variável como private, basta adicionarmos ao seu prefixo um duplo underscore 

class Base():
    def __init__(self):
        self.text = 'Hello, World!'
        self.__bye  = 'See you soon. Take care'

    def sayBye(self):
        print(self.__bye)

class Derived(Base):
    def __init__(self):

        # Chamando o construtor da classe Base.
        Base.__init__(self)
        print('Calling class Base')
        print(self.text)

obj_derived = Derived()
obj_base = Base()

print(obj_base.text)
print(obj_base.sayBye())