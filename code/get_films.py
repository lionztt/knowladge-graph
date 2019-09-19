# 爬虫爬取电影数据
# coding:utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


import urllib.request
import json

films = []
for x in range(1,8):
    films.append('http://swapi.co/api/films/'+str(x)+'/')

headers = {} # 预防反爬机制
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

with open('../data/films.txt','a') as fw:
    for item in films:
        print(item)
        request = urllib.request.Request(url=item, headers=headers)
        response = urllib.request.urlopen(request,timeout=20)
        result = str(response.read(),encoding='utf-8')
        print(result)
        fw.write(result+'\n')