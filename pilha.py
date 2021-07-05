from node import Node

class Pilha:
  def __init__(self):
    self.top = None
    self._size = 0 

  def tamanho(self):
    return  print("A quantidade de livros é" + str(self._size))

  def push(self, book):
    node = Node(book)
    node.next = self.top
    self.top = node
    self._size = self._size + 1
    

  def pop(self): 
    if self._size == 0 :
      return print('A pilha está vazia')
    else: 
      node = self.top
      self.top = self.top.next 
      self._size = self._size - 1
      return node.data

  def imprimirLivros(self):
    books = ""
    pointer = self.top
    while(pointer):
      books = books + str(pointer.data) + "\n"
      pointer = pointer.next
    return print(books)
