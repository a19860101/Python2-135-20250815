import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
my_db = client['my_db']
products = my_db['products']

# products.insert_one({
#     'name': '紅茶',
#     'price': 30
# })

# products.insert_many([
#     {
#         'name':'奶茶',
#         'price': 35
#     },
#     {
#         'name':'珍珠奶茶',
#         'price': 55
#     },
#     {
#         'name': '拿鐵',
#         'price': 80
#     }
# ])

# $gt 大於
datas = products.find({'price': {'$gt': 50}})
# $lt 小於
# datas = products.find({'price': {'$lt': 50}})
# $gte 大於等於
# datas = products.find({'price': {'$gte': 55}})
# $gte 小於等於
# datas = products.find({'price': {'$lte': 55}})
# $eq 等於
# datas = products.find({'price': {'$eq': 55}})



for data in datas:
    print(data)

