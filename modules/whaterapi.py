import requests as req

def getWeatherByCity(city):
  r = req.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=2880a795ad68314c6811453093e38926')
  if r.status_code == 404:
    return 'Local não encontrado'

  json = r.json()
  return 'A temperatura atual em ' + city.title() + ' é: ' + str(json.get('main', {}).get('temp', '0')) + 'ºC'