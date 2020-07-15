import math
import os

os.system('clear')

def porcentagem():

	n1 = float(input("Porcentagem desejada: "))

	n2 = float(input("Valor desejado inteiro: "))

	div = n1 / 100
	multi = div * n2
	print(n1, 'porcento de', n2, 'é:', multi)



def depois_da_porcentagem():

	print('')
	consulta = input('Deseja realizar outra consulta? ').capitalize()
	if consulta == 'S':
		porcentagem()
		depois_da_porcentagem()
	
	elif consulta == 'N':
	   print('Obrigado por utilizar o programa porcentagem')
	   print('')
	   print('Programmed by Silvio Macedo.')
	   exit(0)
	else:
		print('Caractere inválido!...Saindo do programa! ')


porcentagem()
depois_da_porcentagem()