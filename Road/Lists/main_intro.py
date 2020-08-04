# Lists can be written as a list of comma-separated values (items) between square brackets.
# Remember: can contain items of differents types, but usually the items all have the same type.

conj = [5, 6, 7, 8, 10 ,56]
conj2 = conj + [10, 20, 30, 40]

# Using the index for return a specific value

conj[0]
conj[2]

# Slice (return a new list with the request elements (shallow copy of the list))

new = conj[-3:]

# Lists are a mutable type, we can change the value inside

conj[2] = 100
conj[0] = conj[5]

print(conj)