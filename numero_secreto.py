numero_secreto = 24
contador = 0
contador_limite = 3
while contador < 3:
	convidado = int(input( "Tente advinhar numero: "))
  contador += 1
	if convidado == numero_secreto:
	print("Hummm....Advinhou né?!...Baitolão!!")
	break
	else:
		print('Não....')

print("Deu mole mané!!...Tenta de novo!!")
