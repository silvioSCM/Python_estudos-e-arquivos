import sys
import subprocess as sub

print('Olá! o que deseja que seja aberto? Programa "P" ou site "S" ')
comando = input().capitalize()

if comando == "P":
	programa = input('Digite o programa... ')
	sub.Popen(programa)
elif comando == "S":
	site = input('Digite o site...')
	sub.Popen(['xdg-open', site])
else:
	print('Comando inválido! tente de novo.')
