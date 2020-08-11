#   IF 
#   Used to determine the execution of code based on the evaluation of a Boolean expression

variable = int(input('Type some integer: '))

if variable > 0:
    print('This number is greater than 0')
elif variable < 0:
    print('This number is less than 0')
else :
    print('This number is equals zero.')

#   if ...elif ...elif ...elif , in many cases is the substitute for the switch.