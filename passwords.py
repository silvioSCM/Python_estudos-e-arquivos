import os
import getpass

def menu():
	print('')
	print('***************************************')
	print('***************************************')
	print('******PASSWORDS!! QUAL NECESSITA?******')
	print('***************************************')
	print('***************************************')
	print('')
	print('1 - Servidor NFS - Laboratório(user)')
	print("2 - Servidor de PMV's")
	print('3 - Servidor NFS - Laboratório(Server')
	print('4 - Github ')
	print('5 - Megaupload')
	print('6 - Gmail pessoal')
	print('7 - Login na Oracle')
	print('8 - Login Casas Pedro')
	print('9 - Login Cybercook')
	print('0 - Para sair')
	print('')
	print('***************************************')
	print('***************************************')
	print('***************************************')


def escolha_principal():

	escolha = input('Por favor selecione... ')

	if escolha == '1':
		print('A senha é : R5laboratorio')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()
	
	elif escolha == '2':
		print('IP: 201.17.24.9 - A senha é : kzzktturk')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()
	
	elif escolha == '3':
		print('A senha é : consladelr5')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()
	
	elif escolha == '4':
		print('Site: www.github.com - Usuário: silvioSCM - Passw: m@rsh@ll180276')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()

	elif escolha == '5':
		print('Site: //mega.nz - User: silvio.warsoldier@gmail.com - Passwd: m@rsh@ll01')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo....saindo do programa!')
			quit()
	
	elif escolha == '6':
		print('conta: silviomacedo.scm@gmail.com - Passwd - jabiraca01')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()
	
	elif escolha == '7':
		print('user: silviomacedo.scm@gmail.com - Passwd: M@rsh@ll01')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()

	elif escolha == "8":
		print('site: soudecasa.casaspedro.com.br -`Passwd: 03182425')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()


	elif escolha == "9":
		print('site: www.cybercook.com.br - User: silvio.warsoldier@gmail.com - `Passwd: m@rsh@ll01')
		novo = input('Deseja outra consulta?...').upper()
		if novo == 'S':
			os.system('clear')
			menu()
			escolha_principal()
		else:
			print('Você utilizou o passwords de Silvio Macedo...saindo programa!')
			quit()


	elif escolha == '0':
		os.system('clear')
		print('Obrigado... Saindo do programa!')
		print('Programmed by Silvio Macedo')
		exit(0)

os.system('clear')
senha = getpass.getpass('Coloque a senha do arquivo...')
if senha == '0673':
	menu()
	escolha_principal()
else:
	print('Senha Errada!!! Não autorizado!!...Saindo do programa!')
	quit()


escolha_principal()