# 实体在哪个电影中出现过
import json

films = []
characters = []
planets= []
starships = []
vehicles = []
species = []

def addEntity(arr,filepath):
    with open(filepath,'r') as fr:
        for line in fr.readlines():
            tmp =json.loads(line)
            arr.append(tmp)

addEntity(films,'../data/films.txt')
addEntity(characters,'../data/characters.txt')
addEntity(planets,'../data/planets.txt')
addEntity(starships,'../data/starships.txt')
addEntity(vehicles,'../data/vehicles.txt')
addEntity(species,'../data/species.txt')

data = []
def createVector(arr,type,group):
    for item in arr:
        tmp = []
        for film in films:
            flag = False
            for f in film[type+'s']:
                if item['url'] == f:
                    flag = True
                    break
            if flag:
                tmp.append(1)
            else:
                tmp.append(0)
        data.append({
            'name':item['name'],
            'type':type,
            'group':group,
            'vecter':tmp
        })
createVector(characters,'character',0)
createVector(planets,'planet',1)
createVector(starships,'starship',2)
createVector(vehicles,'vehicle',3)
createVector(species,'specie',4)

films =[[films[x]['title'],films[x]['release_date']] for x in range(0,len(films))]
result = {'films':films,'data':data}

with open('../html/timeline.json','w') as fw:
    fw.write(json.dumps(result))

