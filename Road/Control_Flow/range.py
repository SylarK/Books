#   RANGE()
#   Iterate over a sequence of numbers.

for i in range(11):
    print('The number ' + str(i) + ' is greather than ' + str(i-1))

names = ['Dex', 'Floo', 'Ron', 'Harry', 'Patrick']

for i in range(len(names)):
    print(i, 'nome:', names[i])

print(range(10))

print(sum(range(4)))

print(list(range(15)))
