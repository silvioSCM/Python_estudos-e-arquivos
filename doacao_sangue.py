nome = input('Por favor, digite seu nome...')
idade = int(input('Digite sua idade...'))
peso = int(input('Digite seu peso...'))
horas = int(input('Horas dormidas...'))

if idade < 69:
  if peso > 50:
    if horas > 6:
      print('{}, Você está apto para doação de sangue!!'.format(nome))
      print('')
      print('Programmed by Silvio Macedo ')
else:
  print('Infelizmente {}, você não está apto a doar sangue! '.format(nome))
  print('')
  print('Programmed by Silvio Macedo. ')