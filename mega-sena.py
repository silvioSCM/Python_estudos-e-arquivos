from random import randint
import os
import time
total = []

def selecao():

	os.system('clear')
	print('Bem vindo ao simulador de dezenas da mega-sena. ')
	time.sleep(2)
	print('')
	print('Aguarde alguns segundos... ')
	time.sleep(2)

	contador = 0

	while contador < 6:
		total.append(randint(1, 60))
		contador += 1
	total.sort()
	print(f'Os números sugeridos pelo sistema são: {total}')
	print('')
	resp = input('Deseja outra consulta?').upper()
	if resp == 'S':
		total.clear()
		selecao()
	else:
		quit()
selecao()

	    