import sys

#   Built-in exceptions

    #   É possível construir programas que possuem Exceptions personalizadas. Ao invés de utilizar as Exceptions
    #   por default, podemos utilizar as exceptions criadas por nós mesmos.

#while True:
#    try:
#        x = int(input("Type a number greater than 5: "))
#        if (x > 5):
#            print('Ok.')
#            break
#        else :
#            print('The number is not greater than 5, try again... ')
#    except ValueError:
#        print('Hey! You must type a NUMBER! ')

try:
    archive = input("Type a archive name: ")
    f = open(archive + '.txt')
    s = f.read()
    print(s)

except FileNotFoundError:
    print('Don\'t have any file with this name.')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
