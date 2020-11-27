import time

print('Bem vindo!! eu sou Priscila, a assistente A.I..')
time.sleep(2)
print("Por favor...qual o seu nome?")
seu_nome = input()
time.sleep(3)
print(f"{seu_nome},Você acha que o Júlio é baitola?")
baitola = input(f"Responda 'S' ou 'N'..." )
nao_baitola = (baitola)
print("Calculando......")
time.sleep(3)
print("Hummmmmm.....")
time.sleep(3)

if baitola.upper() == "S":
  print("Meus cálculos confirmam que o Júlio é baitola mesmo!!")
  print('''
"Obrigada por participar! A EGB agradece sua sinceridade!!"
''')
elif nao_baitola.upper() == "N":
  print("O calculado é que vc e um baitola igual a ele!!")
  print('''
"Obrigada por participar! A EGB agradece sua sinceridade!!"
''')
else:
  print("Se não quer participar, vai dar meia hora sem relógio!!!")
