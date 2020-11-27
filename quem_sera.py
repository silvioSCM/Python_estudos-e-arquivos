import random
import getpass
import os

print("******************************************")
print("***********Bem vindo ao quiz!!************")
print('******************************************')
print("******************************************")
print("")

enter = getpass.getpass("Pressione <ENTER> para continuar")
os.system('clear')

lista = ["Tem cabeça grande...", "É flamenguista!", "É paraíba!!"]
pessoa = "Daniel"
contador = 0

while contador < 3:
  contador += 1
  print(random.choice(lista))
  convidado = input( "Tente advinhar quem é!!: ").capitalize()
  if convidado == pessoa:
    print("Ah muleke!!! Esse é o 'CABEÇA DE NÓS TODOS!'")
    break
else: 
  print("Você não conhece ninguém mesmo!!...Programa encerrado!!")
