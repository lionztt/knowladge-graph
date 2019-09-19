# 人物处理

import json

fr =open('../data/characters.txt','r')

with open('../data/characters.csv','w') as fw:
    fw.write('name,height,mass,gender,homeworld\n')
    for line in fr.readlines():
        tmp = json.loads(line)
        if tmp['gender'] == 'none':
            tmp['gender'] = 'n/a'
        if tmp['height'] == 'unknown':
            tmp['height'] = '-1'
        if tmp['mass'] == 'unknown':
            tmp['mass'] = '-1'
        fw.write(tmp['name']+','+tmp['height']+','+tmp['mass']+','+tmp['gender'].strip()+','+tmp['homeworld']+'\n')

fr.close()