# Write a Python program to multiplies all the items in a list.

lista_1 = [2,3,5,6,9]

def mult(lista):
    result = 1
    for x in lista: 
        result*=x
    return result

print(mult(lista_1))
