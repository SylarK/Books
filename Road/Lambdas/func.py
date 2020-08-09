#   lambdas in filter()
    # used to select some particular elements from a seq. of elements.

elements = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001]
filtered = filter(lambda x: x >= 2000, elements)
#print(list(filtered))

elements2 = [1,5,6,9,7,8,5,2,3,2,6,5,9,7]
filtered2 = filter(lambda x: x > 5, elements2)
#print(list(filtered2))

#   lambdas in map()
    # user to apply a particular operation to every element in a sequence
    # map( lambda x : operation , sequences)

elements3 = [1,2,3,4,5,6,7,8,9,10]
filtered3 = map(lambda x: x*2, elements3)
#print(list(filtered3))

#   lambdas in reduce()
    # used to apply an operation to every element in a sequence too. But it's differente
    # because have some steps to be followed to compute an output.

    #1 - Define operation on the first 2 elements of the sequence
    #2 - Save
    #3 - Perform the operation with the saved result and the next element
    #4 - Repeat

from functools import reduce
elements4 = [1,2,3,4,5,6,7,8,9,10]
product = reduce(lambda x, y: x*y, elements4)
print(product)