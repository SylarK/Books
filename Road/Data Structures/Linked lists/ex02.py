class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
        def __init__(self):
            self.headval = None

list1 = SLinkedList()
list1.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

#   Ligando o primeiro node com o segundo
list1.headval.nextval = e2

#   Ligando o segundo node com o terceiro
e2.nextval = e3