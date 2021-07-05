from pilha import *


class Livro(Pilha):
  def __init__(self, id, titulo):
    Pilha.__init__ (self)
    self.id = id
    self.titulo = titulo 
  

  def getid(self):
    return self.id

  def getTitulo(self):
    return self.titulo

  def getAutor(self):
    autor = Autor ('id', 'nome')
    self.autor = autor.nome 
    return self.autor

  def imprimirL(self):
    return print ('Livro: ' + self.titulo + " " + 'Autor: ' + self.autor)


class Autor():
  def __init__(self, id, nome): 
    self.__id = id
    self.nome = nome 

  
