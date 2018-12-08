import modules.whaterapi as wapi

repeat = True
validStart = True
validSearch = True

print('\nOLÁ, BEM VINDO AO TEMPYRATURE!\n')
print('> Vamos descobrir a temperatura atual das cidades?')

while validStart == True:
  value = input('> Para começar digite Y ou para sair digite Q: ').lower()
  if value != 'q' and value != 'y':
    print('> Opção inválida, para iniciar digite Y ou digite Q para sair: ')
    continue
  else:
    validStart = False

while repeat == True:
    if value == 'q':
      repeat = False
      continue
    else: 
      value = input('\n> Qual nome da cidade deseja pesquisar a temperatura? ').lower()
      validSearch = True
      print('\n' + wapi.getWeatherByCity(value))
      while validSearch == True:
        value = input('\n> Deseja pesquisar novamente? Digite Y se sim ou Q para sair: ').lower()
        if value != 'q' and value != 'y':
          print('> Opção inválida!')
          continue
        else:
          validSearch = False