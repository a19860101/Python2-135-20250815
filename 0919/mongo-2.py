import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
my_db = client['my_db']
sales = my_db['sales']
#
# sales.insert_many([
#     {
#         'name': '王大明',
#         'money': 12000
#     },
#     {
#         'name': '王大明',
#         'money': 9900
#     },
#     {
#         'name': '陳小美',
#         'money': 68000
#     },
#     {
#         'name': '王大明',
#         'money': 1500
#     },
#     {
#         'name': '王大明',
#         'money': 6000
#     },
#     {
#         'name': '陳小美',
#         'money': 36000
#     }
# ])

pipline = [
    # step1 比對、篩選
    # {
    #     '$match':{'name':'陳小美'}
    # },
    # step2 分組
    {
        '$group': {
            '_id':'$name',
            '總業績':{
                '$sum':'$money',
            },
            '平均業績':{
                '$avg': '$money'
            }
        }
    },
    # step3 排序
    {
        '$sort': {
            'money': -1
        }
    }
]

result = sales.aggregate(pipline)

# result = sales.find()
for r in result:
    print(r)