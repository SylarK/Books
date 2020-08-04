#Write a Python program to sum all the items in a list.

list_ex = [5,5,5,3,6,2]

def sum_list(lista):
    sum = 0
    for x in lista:
        sum+=x
    return sum

print(sum_list(list_ex))