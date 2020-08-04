#   Methods with Lists in Python

#List.append(obj) - add a obj into List
list_ap = ['apple', 'slice', 'man']
list_ap.append('kirk')


#List.count(obj) - return how many times the object occurs in list
list_count = [10,20,30,30,40,50,50,50,10]
print(list_count.count(10))

#List.extend(seq) - add one obj into other obj
list_1 = ['The', 'first']
list_2 = ['time', 'that']
list_1.extend(list_2)

#List.index(obj) - return the index of the obj
print('The apple is in the index : ' + str(list_ap.index('apple')))

#List.insert(obj) - insert a object into a specific index
list_ap.insert(2, 'lemon')

#List.pop(obj=list[-1]) - remove and return the last value (can use without the index or with index)
list_ap.pop()
list_ap.pop(0)

#List.remove(obj) - remove a specific obj 
list_1.remove('first')

#List.reverse() - invert the list
list_ap.reverse()

#List.sort() - organize 
list_number = [2,50,6,0,89,6,2,2,3,6]
list_number.sort()
print(list_number)

