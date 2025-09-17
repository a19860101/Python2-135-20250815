import pymongo
from bson import ObjectId

# database -> table -> column
# database -> collection -> document -> field
client = pymongo.MongoClient('mongodb://localhost:27017/')


testdb = client['testdatabase']
test_collection = testdb['products']

# 新增單筆資料
# test_collection.insert_one({
    # '_id': 2,
    # 'name': '咖啡',
    # 'price': '30'
# })

# 新增多筆資料
# test_collection.insert_many([
#     {
#         '_id': 1,
#         'name' : 'asdf',
#         'price': 45
#     },{
#         '_id': 2,
#         'name' : '45235',
#         'price': 40
#     },{
#         '_id': 3,
#         'name' : 'test',
#         'price': 45
#     },{
#         '_id': 4,
#         'name' : '測試',
#         'price': 55
#     }
# ])

# 刪除單筆資料
# test_collection.delete_one({
#     'name': '紅茶'
# })

# 刪除多筆資料
# test_collection.delete_many({
#     'name': '紅茶'
# })


## 當有自動產生_id的狀態時，可用下列方式刪除
### method 1
### 先尋找資料再刪除
# delete_data = test_collection.find_one({'name':'咖啡'})

# print(delete_data['_id'])
# print(delete_data['name'])
# print(delete_data['price'])
# test_collection.delete_one({'_id': delete_data['_id']})

### 直接透過ObjectID刪除
### 需引入bson的ObjectID
# test_collection.delete_one({'_id': ObjectId('68caa7326f3a9b18ddf42bce')})

# 更新單筆資料
# test_collection.update_one(
#     {'_id': 3},
#     {'$set':{'name': '測試123'}}
# )

# 更新多筆資料
# test_collection.update_many(
#     {'name':'更新測試'},
    # {'$set':{'qty': '10'}}
# )

# test_collection.update_one(
#     {'_id': 1},
#     {'$set':{'price':'45'}}
# )

# test_collection.update_many(
#     {},
#     {'$set':{'qty':'100'}}
# )

# test_collection.update_many(
#     {},
#     {'$push':{'datas': 'b'}}
# )

# test_collection.update_many(
#     {},
#     {'$push':{'datas': {'$each': ['c','d']}}}
# )

# test_collection.update_many(
#     {},
#     {'$pull':{'datas': 'd'}}
# )

test_collection.update_many(
    {},
    {'$unset':{'qty':''}}
)

# 移除資料表
test_collection.drop()

for prod in test_collection.find():
    print(prod)
#
# print(testdb)
print(client.list_database_names())