def forma(self):
    self.clear()
    self.penup()
    self.setpos(0, -100)
    self.pendown()
    self.fillcolor("red")
    self.begin_fill()
    self.circle(20)
    self.end_fill()
    self.penup()
    self.circle(20,180)
    self.right(90)
    self.forward(20)
    self.right(90)
    self.fillcolor("black")
    self.begin_fill()
    self.pendown()
    self.circle(20,90)
    self.forward(50)
    self.circle(20,180)
    self.forward(50)
    self.circle(20,90)
    self.end_fill()
    self.penup()
    self.setpos(0, -110)
    self.pendown()
    self.forward(125)
    self.circle(20,130)
    self.forward(168)
    self.circle(40,100)
    self.forward(168)
    self.circle(20,130)
    self.forward(130)
    self.penup()
    self.home()