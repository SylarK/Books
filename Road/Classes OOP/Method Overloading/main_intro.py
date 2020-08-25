#   Method Overloading
#   Como muitas outras linguagens, python não aceita o método overloading por default. Mas é possível ativa-lo de diversas maneiras.
#   Uma das maneiras é utilizar a mesma função para fazer diversas coisas, através por exemplo de uma verificação do tipo de argumento inserido
#   Não é tão indicado mas ficaria dessa forma :

#def countOrsay(datatype, *args):
#    if datatype == 'str':
#        answer = ''
    
#    if datatype == 'int':
#        answer = 0

#    for x in args:
#        answer = answer + x
    
#    print(answer)


#countOrsay('int', 2, 6, 8, 10)
#countOrsay('str', 'Hello everyone!', ' The ', ' winter', ' is', ' coming', ' !')

#   Outra forma seria utilizando Multiple Dispatch Decorator
#   pip3 install multipledispatch

#   Ficaria dessa forma uma aplicação

from multipledispatch import dispatch

@dispatch(int, int)
def sum(num1, num2):
    answer = num1 + num2
    print(answer)

@dispatch(int, int, int)
def sum(num1, num2, num3):
    answer = num1 + num2 + num3
    print(answer)

@dispatch(float, float)
def sum(num1, num2):
    answer = (num1 + num2) * 2
    print(answer)

sum(5,10)
sum(10,10,10)
sum(5.0,3.0)