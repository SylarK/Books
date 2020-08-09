#   Dictionaries
#   Are indexed by keys, which can be any immutable type.
#   All keys are unique in the dictionaries.
    #   list(d) - dictionary return a list of all the keys used in the dictionary

data = {'John':455620, 'Julia':998653}
data['Joshua'] = 999999

#print(list(data))
#print(sorted(data))

print('John' in data)
print({x: x**2 for x in (5,10,20,30)})
print(dict(car='e350', cilinder='55x80'))