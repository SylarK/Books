#   It's important remember that lambda function return a function

x = 'The art of programming'
(lambda  x: print(x))(x)

#   We are defining a lambda and calling it immediately by
#   passing the string as an argument. (This is something called an IIFE)
