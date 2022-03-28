from fichers.maike import *

def fellipeLetra1(self, pos):
  self.setpos(pos)
  self.left(90)
  self.forward(55)
  self.right(90)
  self.forward(30)
  self.back(30)
  self.left(90)
  self.back(20)
  self.right(90)
  self.forward(20)
  self.penup()
  self.home()

def fellipeLetra2(self,pos):
  maikeLetra5(self,pos)
  

def fellipeLetra3(self,pos):
  self.setpos(pos)
  self.left(90)
  self.pendown()
  self.forward(55)
  self.back(50)
  self.right(90)
  self.forward(30)
  self.penup()
  self.home()

def fellipeLetra4(self,pos):
  fellipeLetra3(self,pos)

def fellipeLetra5(self,pos):
  maikeLetra3(self,pos)


def fellipeLetra6(self,pos):
  self.setpos(pos)
  self.left(90)
  self.forward(20)
  self.right(90)
  self.pendown()
  self.circle(20,180)
  self.left(90)
  self.forward(60)
  self.penup()
  self.home()

def fellipeLetra7(self,pos):
  maikeLetra5(self,pos)
