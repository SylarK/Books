#   Recursion Function
#   When the function call itself instead other functions.

#   O exemplo mais dado para funções recursivas é utilizar uma conta fatorial. 
#   Sem recursão : 

print('*'*20 + ' Factorial ' + '*'*20)
n = int(input('Type a number: '))

def fatorial(n):
    if n > 2:
        sum = 1
        n = range(n + 1)
        for i in n :
            if i < 2:
                pass
            else:
                sum = sum * i
        return sum
    
    else:
        return 1        

print('The result is : ' + str(fatorial(n)))

#   Com recursão

def fatorial_recursion(n):
    if n < 2:
        return 1
    else:
        return n * fatorial_recursion(n - 1)
    

print('The result is : ' + str(fatorial_recursion(n)))


#   PROS
    #   Código limpo
    #   Facilidade ao digitar
    #   Aplicável a problemas simples

# CONTRAS
    #   Para recursões longas o entendimento da lógica tende a ser extremamente complexo
    #   Funções recursivas tendem a exigir mais da memória do computador
    #   Por a lógica ser um pouco mais complexa, funções recursivas são mais difíceis de debugar