import requests

resp = requests.get("https://swapi.co/api/people/3/

data = resp.json()
resp2 = requests.get(data['homeworld'])
data2 = resp2.json()

print('el personaje %s nacio en el año %s y vive en un planeta llamado %s' % (data['name'], data['birth_year'], data2['name']))