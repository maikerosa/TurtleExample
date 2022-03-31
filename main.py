def exibirMenu():
  print("-"*30)
  print(" "*7 , "Menu de Opções: ")
  print("⚠️  Maximize o Python Turtle G.")
  print("0 - Sair")
  print("1 - Desenhar Nome(s): ")
  print("2 - Desenhar Forma: ")
  print("-"*30)

from MinhasClasses import MeuTurtle
import os


def turtleExample():
  p1 = MeuTurtle()
  op = -1

  while(op != 0):
    os.system('clear')
    exibirMenu()
    try:
      op = int(input("Digite a opção: "))
    except:
      print("Formato Inválido.")
      turtleExample()

    if op == 1:
      try:
        esc = int(input('Escolha o nome: (1/2) '))
      except:
        print("Formato Inválido.")
        turtleExample()
      while esc < 1 or esc > 2:
        try:
          esc = int(input('Escolha o nome: (1/2) '))
        except:
          print("Formato Inválido.")
          turtleExample()
      p1.desenharNomes(esc)
    elif op == 2:
      p1.desenharForma()
    elif op == 0:
      print("Tudo parado.")
      p1.saida()
    else:
      print("Opção inválida!")

    
# start
turtleExample()