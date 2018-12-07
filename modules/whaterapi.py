import requests as req

def getPlaceholderTest():
  r = req.get('https://jsonplaceholder.typicode.com/todos/1')
  json = r.json()
  return 'Titulo teste é: ' + json.get('title', 'Not found')