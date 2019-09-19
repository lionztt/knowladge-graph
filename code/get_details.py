# 下载其他信息
import urllib.request
import json

headers = {} # 预防反爬机制
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

films = []
with open('../data/films.txt','r') as fr:
    for line in fr.readlines():
        # print(line)
        line = json.loads(line)
        films.append(line)

# 爬取5大类信息
targets = ['characters', 'planets', 'starships', 'vehicles', 'species']
for target in targets:
    data = []
    with open('../data/'+target+'.txt','w') as fw:
        for item in films:
            tmp = item[target] # 取key对应的值（人的url）
            for t in tmp:
                if t in data:
                    continue
                else:
                    data.append(t)
                while 1:
                    print(t)
                    try:
                        request = urllib.request.Request(url=t, headers=headers)
                        response = urllib.request.urlopen(request,timeout=20)
                        result = str(response.read(),encoding='utf-8')
                    except Exception as e:
                        continue
                    else:
                        fw.write(result+'\n')
                        break
                    finally:
                        pass
    print(len(data),target)