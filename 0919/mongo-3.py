import pymongo
from bson import ObjectId
import requests

url = 'https://media.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json'

res = requests.get(url,verify=False)
res.encoding='utf-8-sig'
jsonfile = res.json()

result = jsonfile['XML_Head']['Infos']['Info']
#
client = pymongo.MongoClient('mongodb://localhost:27017/')
my_db = client['my_db']
scenic = my_db['scenic']


# scenic.insert_many(result)

query = {
    '$and':[
        {'Region': '桃園市'},
        {'Town': '桃園區'}
    ]
}

# 只顯示Name跟Toldescribe兩個field
# datas = scenic.find({'Region':'臺北市'},{'_id':0,'Name':1,'Toldescribe':1})
# datas = scenic.find({'Region':{'$regex':'桃園'}},{'_id':0,'Name':1,'Region':1})
# datas = scenic.find({'Name':{'$regex':'宮$'}},{'_id':0,'Name':1,'Region':1})
datas = scenic.find(query,{'_id':0,'Name':1,'Region':1})
for s in datas:
    print(s)

# scenic.drop()

client.close()


