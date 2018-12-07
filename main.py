import modules.whaterapi as wapi

print('Olá, bem vindo ao TEMPYRATURE! \n')
city = input('Qual a cidade deseja saber a temperatura? ')
print('\n' + wapi.getWeatherByCity(city) + '\n')
