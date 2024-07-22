from __future__ import annotations
# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
# Lifo e fifo
# pilaha e fila

# LIFO (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Vídeo:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(n) Tempo Linear

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ Legal (LIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11)
#  0  1  2  3  4  5  6  7  8  9  10  11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ultimo_removido = lista.pop()
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Último: ', ultimo_removido)
print('Lista: ', lista)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🚫 Ruim (FIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 10)
#  0   1  2  3  4  5  6  7  8  9  10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 11)
#  0   1   2  3  4  5  6  7  8  9  10 11
# [10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_removido = lista.pop(0)  # 11
#  0   1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Primeiro: ', primeiro_removido)  # 11
print('Lista:', lista)  # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()


# FIFO (First In First Out)
# Filas (queue)
# Significa que o primeiro ite a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(1) Tempo constante

# ✅ Legal (FIFO com deque)

fila_correta: deque[int] = deque()
fila_correta.append(3) # Adiciona no final
fila_correta.append(4) # Adiciona no final
fila_correta.append(5) # Adiciona no final
fila_correta.appendleft(2) # Adiciona no começo
fila_correta.appendleft(1) # Adiciona no começo
fila_correta.appendleft(0) # Adiciona no começo
print(fila_correta) # deque([0, 1, 2, 3, 4, 5])
fila_correta.pop() # 5
fila_correta.popleft() # 0
print(fila_correta) # deque([1, 2, 3, 4])

# Stack - aula youtube

from typing import List
from copy import deepcopy

stack: List = []

stack.append(['A'])
stack.append(['B'])
stack.append(['C'])

print('FOR:')
for item in stack[::-1]:
    print(item)

# shallow copy
# stack_copy = stack.copy()
# deep copy
stack_copy = deepcopy(stack)

print('\nWHILE:')
while stack_copy:
    item = stack_copy.pop()
    item += ['M']
    print(item)

print('\nSUA PILHA:', stack)

# stack class
# append, pop, peek
# iterar com for e com while
from typing import List, Any, Deque

class Stack:
    """
    Uma classe que representa uma stack.

    Podemos criar uma classe para representação de uma stack. Isso nos permite
    expor apenas os métodos que queremos, da maneira que desejarmos.

    Por exemplo: na classe a seguir, vamos expor apenas os métodos append, pop (sem
    permitir índice) e peek (o mesmo que pop, mas sem eliminar o topo da pilha).

    Também implementamos os métodos dunder a seguir:
        - __repr__: para representação da classe
        - __iter__ e __next__: para iteração com for
        - __bool__: para iteração com while. O método __bool__ retorna True se
        nossa stack tiver valores e False se não.
    """
    def __init__(self):
        self.__data:List[Any] = []
        self.__index = 0

    def push(self, item: Any) -> None:
        self.__data.append(item)

    def pop(self) -> Any:
        return self.__data.pop()
    
    def peek(self) -> Any:
        if not self.__data:
            return []
        return self.__data[-1]
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__data})"
    
    def __iter__(self) -> Stack:
        self.__index = len(self.__data)
        return self
    
    def __next__(self) -> Stack:
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__data[self.__index]
    
    def __bool__(self) -> bool:
        return bool(self.__data)
    

# Queue - aula youtube

# fila com classes
EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

class EmptyQueueError(Exception):
    ...
class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node

    def __repr__(self) -> str:
        return f'{self.value}'

    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)
    
class Queue:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0

    def push(self, node_value: Any):
        new_node = Node(node_value)
        if not self.first:
            self.first = new_node
        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self._count += 1

    def pop(self) -> Node:
        if not self.first:
            raise EmptyQueueError('Empty queue')
        first = self.first

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)
        self._count -= 1
        return first
    
    def peek(self) -> Node:
        if not self.first:
            raise EmptyQueueError('Empty queue')
        return self.first 

    def __len__(self) -> int:
        return self._count
    
    def __bool__(self) -> bool:
        return bool(self._count)
    
    def __iter__(self) -> Queue:
        return self
    
    def __next__(self) -> Any:
        try:
            next_value = self.pop()
            return next_value
        except EmptyQueueError:
            raise StopIteration

    def __repr__(self) -> str:
        if not self.first:
            return f'{self.__class__.__name__}()' 
        return f'{self.__class__.__name__}({self.first}, {self.last})'

if __name__ == '__main__':
    print('Stack Class')
    stack_obj = Stack()
    stack_obj.push('A')
    stack_obj.push('B')
    stack_obj.push('C')

    top_item = stack_obj.pop()

    print(top_item, stack_obj)

    print('FOR:')
    for item in stack_obj:
        print(item)

    stack_obj_copy = deepcopy(stack_obj)


    print('\nWHILE:')
    while stack_obj_copy:
        print(stack_obj_copy.pop())

    print('\nPILHA ORIGINAL:', stack_obj)
    print('\nPILHA COPIA:', stack_obj_copy)

    print('Queue Class:')
    queue_obj = Queue()
    queue_obj.push('A')
    queue_obj.push('B')
    queue_obj.push('C')
    queue_obj.push('D')
    print(queue_obj)
    print(queue_obj.pop())
    print(queue_obj)
    for item in queue_obj:
        print(item)
    try:
        print(queue_obj.pop())
    except:
        print('Fila é esvaziada após o for')

    # fila com deque
    queue_deque:Deque[Any] = deque()
    queue_deque.append('A')
    queue_deque.append('B')
    queue_deque.append('C')
    queue_deque.append('D')
    print(f'Removido {queue_deque.popleft()}')

    for item in queue_deque:
        print(item)

    print(f'Removido {queue_deque.popleft()}')
