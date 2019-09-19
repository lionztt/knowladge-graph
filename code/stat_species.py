# 种族处理

import json

fr =open('../data/species.txt','r')

with open('../data/stat_species.csv','w') as fw:
    fw.write('name,height,lifespan,classification\n')
    for line in fr.readlines():
        tmp = json.loads(line)
        if tmp['classification'] == 'mammals':
            tmp['classification'] = 'mammal'
        if tmp['classification'] == 'reptilian':
            tmp['classification'] = 'reptile'
        if tmp['average_height'] in ['n/a','unknown']:
            tmp['average_height'] = '-1'
        if tmp['average_lifespan'] in ['unknown','indefinite']:
            tmp['average_lifespan'] = '-1'
        fw.write(tmp['name']+','+tmp['average_height']+','+tmp['average_lifespan']+','+tmp['classification']+'\n')

fr.close()