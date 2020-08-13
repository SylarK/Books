#   We use def for create any function

def fib(n):
#DEF introduces a function 

    a, b = 0, 1

    while(a < n):
        print(a, end=' ')
        a, b = b, a+b

    print()


fib(2000)
f = fib
f(200)

#default arguments

def times100(n=20):
    return n * 100

print(times100(5))
print(times100())

def make_incrementor(n):
    return lambda x: x + n

def f(pos1, pos2, pos_or_kwd, *, kwd1, kwd2):
    print('')    