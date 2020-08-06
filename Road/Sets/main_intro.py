#   SET - is a unordered collection with no duplicate elements ( eliminate duplicate entries ).
#         We can use curly braces {} or the set() function to create sets (but to create a empty set we have to use the function)

sports = {'basketball', 'tennis', 'fotball', 'baseball', 'golf','baseball', 'tennis', 1, 10, 1, 20}

var1 = set('Macarronada')
var2 = set('Massa de Correia')
print(var2 - var1)
print(var2 & var1)
print(var2 ^ var1) # var1 or var2 but not in both

for x in var1:
    print(x)

print('tennis' in sports)

#   To add one item to a set use the add() method.
#   To add more than one item to a set use the update() method.

sports.add('Ping Pong')