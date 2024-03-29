# 整理数据到前端

import json

films = {}
characters = {}
planets = {}
starships = {}
vehicles = {}
species = {}

fr = open('../data/films.txt', 'r')
for line in fr.readlines():
    tmp = json.loads(line)
    films[tmp['url']] = tmp
fr.close()
fr = open('../data/characters.txt', 'r')
for line in fr.readlines():
    tmp = json.loads(line)
    characters[tmp['url']] = tmp
fr.close()
fr = open('../data/planets.txt', 'r')
for line in fr.readlines():
    tmp = json.loads(line)
    planets[tmp['url']] = tmp
fr.close()
fr = open('../data/starships.txt', 'r')
for line in fr.readlines():
    tmp = json.loads(line)
    starships[tmp['url']] = tmp
fr.close()
fr = open('../data/vehicles.txt', 'r')
for line in fr.readlines():
    tmp = json.loads(line)
    vehicles[tmp['url']] = tmp
fr.close()
fr = open('../data/species.txt', 'r')
for line in fr.readlines():
    tmp = json.loads(line)
    species[tmp['url']] = tmp
fr.close()

nodes = []
links = []

for key, value in films.items():
    nodes.append({'id': value['title'], 'class': 'film', 'group': 0, 'size': 20})
    # characters
    for item in value['characters']:
        if item in characters:
            links.append({'source': value['title'], 'target': characters[item]['name'], 'value': 3})
    # planets
    for item in value['planets']:
        if item in planets:
            links.append({'source': value['title'], 'target': planets[item]['name'], 'value': 3})
    # species
    for item in value['species']:
        if item in species:
            links.append({'source': value['title'], 'target': species[item]['name'], 'value': 3})
    # starships
    for item in value['starships']:
        if item in starships:
            links.append({'source': value['title'], 'target': starships[item]['name'], 'value': 3})
    # vehicles
    for item in value['vehicles']:
        if item in vehicles:
            links.append({'source': value['title'], 'target': vehicles[item]['name'], 'value': 3})

for key, value in characters.items():
    nodes.append({'id': value['name'], 'class': 'character', 'group': 1, 'size': 5})
    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
    # planets
    if value['homeworld'] in planets:
        links.append({'source': value['name'], 'target': planets[value['homeworld']]['name'], 'value': 3})
    # species
    for item in value['species']:
        if item in species:
            links.append({'source': value['name'], 'target': species[item]['name'], 'value': 3})
    # starships
    for item in value['starships']:
        if item in starships:
            links.append({'source': value['name'], 'target': starships[item]['name'], 'value': 3})
    # vehicles
    for item in value['vehicles']:
        if item in vehicles:
            links.append({'source': value['name'], 'target': vehicles[item]['name'], 'value': 3})

for key, value in planets.items():
    nodes.append({'id': value['name'], 'class': 'planet', 'group': 2, 'size': 16})
    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
    # characters
    for item in value['residents']:
        if item in characters:
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in starships.items():
    nodes.append({'id': value['name'], 'class': 'starship', 'group': 3, 'size': 8})
    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
    # characters
    for item in value['pilots']:
        if item in characters:
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in vehicles.items():
    nodes.append({'id': value['name'], 'class': 'vehicle', 'group': 4, 'size': 8})
    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
    # characters
    for item in value['pilots']:
        if item in characters:
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in species.items():
    nodes.append({'id': value['name'], 'class': 'species', 'group': 5, 'size': 14})
    # planets
    if value['homeworld'] in planets:
        links.append({'source': value['name'], 'target': planets[value['homeworld']]['name'], 'value': 3})
    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})
    # characters
    for item in value['people']:
        if item in characters:
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

fw = open('../html/starwar.json', 'w')
fw.write(json.dumps({'nodes': nodes, 'links': links}))
fw.close()
