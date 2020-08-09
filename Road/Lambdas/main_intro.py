#   Lambdas (small anonymous functions)
#   This functions return the sum of its two arguments.
#   Can be used wherever function objects are required. Restricted to a single expression
#   Can have any number of parameters but the function body can only contain one expression

    #   lambda p1, p2: expression


def make_incrementor(n):
    return lambda x: x + n

x = make_incrementor(10)
#print(x(0))
#print(x(10))
#print(x(20))
#print(x(30))

