import csv

# with open('./Scenic_Spot_C_f.csv','r',encoding='utf-8')as f:
#     csvfile = csv.reader(f)
#
#     print(csvfile)
#     for c in csvfile:
#         print(c)


with open('./Scenic_Spot_C_f.csv','r',encoding='utf-8')as f:
    csvfile = csv.DictReader(f)
    for data in csvfile:
        # print(data)
        print(data['Name'],':',data['Add'])