import pygame
import os
import time

command = ''
started = False
conversa = False
boia = False
escada = True
os.system('clear')
print('Olá! eu sou \033[1:33mJúlio Rogério\033[0:37m, auxiliar técnico da CLD/R5.')
time.sleep(1)
print('Hoje teremos um dia de rota no R5, e você será minha compahia.')
print('')
time.sleep(1)
print('Para começar baitola, qual o seu nome? ')
nome = str(input().capitalize())
feios = ['Amilton', 'Genilson', 'Flávio']
try:
    if nome in feios:
        raise NameError('Xiiii')
except NameError:
    print('O programa não gostou do seu nome...Muito feio!! ')
    time.sleep(1)
print('')
print(f'{nome},vamos começar! Basta digitar os comandos, e vamo embora antes que dê ruim ')

while True:

    command = input('Viatura CLD/R5 >> ').lower()
    if command == 'andando':
        if started:
            print('Já estou andando baitola!! Vai dar 1/2 hora sem relógio!!')
        else:
            started = True
            print('Carro andando baitola!!')

    elif command == 'pare':
        if not started:
            print('Caraca!! já tô parado aqui mó tempão seu baitola!!!')
        else:
            started = False
            print('Já parei no ponto baitola!')

    elif command == 'buzine':
        print("Sai do caminho!! é um cú d'água mesmo!! ")
        time.sleep(1)
        print('Como tem neguinho fazendo merda na pista!!')

    elif command == 'ajuda':
        print('''
andando - Carro andando
pare - Carro parado
buzine - Buzina
sair - Sair do game
xingar - Júlio xinga os outros motoristas!
julio - Você chama o Júlio
ajuda - Ajuda do game
fome - Verifica se o Júlio está com fome!
faq - Documento do game
radio - Rádio do Baitola
''')

    elif command == 'xingar':
        print('Vai chupar um canavial de rola seu baitola!! ')
        time.sleep(1)
        print('Gosta de laranja? Vou te arrumar um saco pra você chupar!! E GRANDE!! ')
        time.sleep(1)
        print('Vai dar 1/2 hora sem relógio seu baitola! ')
        time.sleep(1)
        print('Ah!! Vê se vai num rodízio de rola seu baitola!!!')

    elif command == 'sair':
        print('')
        print('Eu Júlio espero que você tenha curtido o nosso passeio baitola!! ')
        print('')
        pygame.init()
        pygame.mixer_music.load('julio_falando.mp3')
        pygame.mixer_music.play()
        print(f'{nome}, Obrigado por brincar!! Programmed by Silvio Macedo!! ')
        time.sleep(2)
        break

    elif command == 'escada':
        if started:
            print('Tem que parar o carro para botar a escada baitola!! ')
        else:
            if not started:
                print('Vou botar a escada baitola!!. Deixa que depois eu tiro!! ')

    elif command == 'radio':
    	print('~' * 30)
    	print('Selecione a música...')
    	print('1 - Bibaitola')
    	print('2 - Chá de baitola')
    	print('3 - Holiday foi muito')
    	print('0 - Desligar rádio / sair')
    	print('~' * 30)
    	resp = int(input('Selecione..'))
    	if resp == 1:
    		pygame.init()
	    	pygame.mixer_music.load('baitola.mp3')
	    	pygame.mixer_music.play()
    #        pygame.event.wait()

    	elif resp == 2:
    		pygame.init()
    		pygame.mixer_music.load('cha_de_baitola.mp3')
    		pygame.mixer_music.play()
    	
    	elif resp == 3:
    		pygame.init()
    		pygame.mixer_music.load('Holiday_foi_muito.mp3')
    		pygame.mixer_music.play()
    	
    	elif resp == 0:
    		pygame.init()    		
    		pygame.mixer_music.stop()
    		continue
    		    	
    	else:
    		print('Baitola, esse sucesso NÃO TEM!!! Liga de novo e selecione um da lista!!! SEU BAITOLA!!')
    	

    elif command == 'julio':
        if conversa:
            print('Ah!! já vi que vou ter que matar uma meia dúzia hoje!! Só enchendo barra de status!! ')
            conversa = False
        else:
            conversa = True
            print('Fala, o que tú qué baitola!! ')

    elif command == 'fome':
        if boia:
            print('Barriga tá roncando!! Parece que dormi amarrado!! ')
            boia = False
        else:
            boia = True
            print('Caraca que fome!!! Tá querendo me matar de fome baitola?? ')

    elif command == 'faq':
        file = open('baitola_help.txt', 'r')
        print(file.read())
    else:
        print('Não entendi baitola!! Simulou infarto? Peidou? - Digite "ajuda" para comandos!!')
