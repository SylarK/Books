#   Linked Lists
#   São uma coleção ordenada de objetos.
#   Diferença entre listas normais : Na maneira com que armazena os elementos na memória.
#   Cada Linked List possui um node, que possui um Data e um Next (que seria uma referência ao próximo Data). Inicia-se no head.
#   O uso é gigante, pode-se utilizar para implementar queues ou stacks.
#   Em python, para se utilizar as linked list é necessário utilizar collections.deque

from collections import deque
a = deque(['a', 'b','c'])
b = deque('abcde')
c = deque([{'data':'a'}, {'data':'b'}])

a.append('d')
a.appendleft('0')
a.popleft()
a.append('fork')
a.pop()

#   Using linked list for implement a queues
#   queues are FIFO(First In , First Out)
#   Ex. Restaurant
queue = deque()
queue.append('Joshua')
queue.append('Fred')
queue.append('Marry')
queue.append('Jess')
queue.popleft()
queue.popleft()
queue.popleft()

#   Using linked list for implement a stack
#   stacks are LIFO(Last In, First Out)
#   Ex. History

history = deque()

history.appendleft('https://amadodev.com/')
history.appendleft('https://amadodev.com/portfolio/weatherapp')
history.appendleft('https://amadodev.com/portfolio/calculatorapp')

#   Agora o usuário, após olhar as aplicações, quer voltar a página principal. Para isso removemos elementos seguindo a regra LIFO.
history.popleft() #'https://amadodev.com/portfolio/calculatorapp'
history.popleft() #'https://amadodev.com/portfolio/weatherapp'




