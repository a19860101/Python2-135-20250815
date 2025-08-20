import csv

# with open('mrt.csv','r',encoding='cp950') as f:
#     result = csv.reader(f)
#     print(result)
#     for data in result:
#         print(data)

f = open('mrt.csv','r',encoding='cp950')
result = csv.reader(f)
for data in result:
    print(data)

f.close()