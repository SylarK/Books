#   Write a Python program to remove duplicates from a list.

original = [10,10,2,2,3,6,5,5,9,10,12,56,56]

for x in original:
    if original.count(x) > 1 :
        original.remove(x)

print(original)
