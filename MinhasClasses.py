from turtle import Turtle
from fichers.maike import *
from fichers.fellipe import *
from fichers.forma import *
from fichers.saida import *

class MeuTurtle(Turtle):
  def __init__(self):
    super().__init__("classic")
    self.color("black")
    self.pensize(2)
    self.penup()

  def saida(self):
    self.clear()
    sair(self)

  def desenharForma(self):
    forma(self)

    
  def desenharNomes(self, nome):
    self.penup()
    self.setpos(-200.00,-100)
    lista = []
    if nome == 1:
      self.clear()
      self.pendown()
      self.forward(400)
      for x in range(1, 6):
        if x == 1:
          self.back(120)
        elif x == 2:
          self.back(50)
        elif x == 3:
          self.back(25)
        elif x == 4:
          self.back(50)
        elif x == 5:
          self.back(60)
        lista.append(self.pos())
      maikeLetra1(self, lista[4])
      maikeLetra2(self, lista[3])
      maikeLetra3(self, lista[2])
      maikeLetra4(self, lista[1])
      maikeLetra5(self, lista[0])
    elif nome == 2:
      self.clear()
      self.pendown()
      self.forward(420)
      for x in range(1, 8):
        if x == 1:
          self.back(90)
        elif x == 2:
          self.back(40)
        elif x == 3:
          self.back(25)
        elif x == 4:
          self.back(50)
        elif x == 5:
          self.back(60)
        elif x == 6:
          self.back(60)
        else:
          self.back(45)
        lista.append(self.pos())
      fellipeLetra1(self, lista[6])
      fellipeLetra2(self, lista[5])
      fellipeLetra3(self, lista[4])
      fellipeLetra4(self, lista[3])
      fellipeLetra5(self, lista[2])
      fellipeLetra6(self,lista[1])
      fellipeLetra7(self, lista[0])

