# 数据清洗
import json

fr = open('../data/films.txt','r')

with open('../data/stat_basic.csv','a') as fw:
    fw.write('title,key,value\n')
    for line in fr.readlines():
        tmp = json.loads(line)
        fw.write(tmp['title']+','+'characters,'+str(len(tmp['characters']))+'\n') # 统计各个电影人物数量
        fw.write(tmp['title'] + ',' + 'planets,' + str(len(tmp['planets']))+'\n')  # 统计各个电影人物数量
        fw.write(tmp['title'] + ',' + 'starships,' + str(len(tmp['starships']))+'\n')  # 统计各个电影人物数量
        fw.write(tmp['title'] + ',' + 'vehicles,' + str(len(tmp['vehicles']))+'\n')  # 统计各个电影人物数量
        fw.write(tmp['title'] + ',' + 'species,' + str(len(tmp['species']))+'\n')  # 统计各个电影人物数量

fr.close()
