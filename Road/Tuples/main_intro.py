#   Tuples - consists of a number of values separated by commas
#   obs: Tuples are immutable, but they can contain mutable objects
#        output tuples are always enclosed in parentheses

t = 123,456,789, 'Hello, World', (1,2,3,4,5,6),[1,1,2],[2,3,3]
t[5][0] = 10

empty = ()
single = 'single',

print(len(empty))
print(len(single))
print(t)