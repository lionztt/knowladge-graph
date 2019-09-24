# 整理点信息框

import json

data ={}
with open('../data/films.txt','r') as fr:
    for line in fr.readlines():
        tmp = json.loads(line)
        data[tmp['title']] = tmp
with open('../data/characters.txt', 'r') as fr:
    for line in fr.readlines():
        tmp = json.loads(line)
        data[tmp['name']] = tmp
with open('../data/planets.txt', 'r') as fr:
    for line in fr.readlines():
        tmp = json.loads(line)
        data[tmp['name']] = tmp
with open('../data/starships.txt', 'r') as fr:
    for line in fr.readlines():
        tmp = json.loads(line)
        data[tmp['name']] = tmp
with open('../data/vehicles.txt', 'r') as fr:
    for line in fr.readlines():
        tmp = json.loads(line)
        data[tmp['name']] = tmp
with open('../data/species.txt', 'r') as fr:
    for line in fr.readlines():
        tmp = json.loads(line)
        data[tmp['name']] = tmp

fw = open('../html/all.json', 'w')
fw.write(json.dumps(data))
fw.close()