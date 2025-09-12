# 201

"""
請撰寫一程式，讀取文化部展覽資訊read.json，
請將其中title（活動名稱）、showUnit（演出單位）、
startDate（活動起始日期）、endDate（活動結束日期）
等四個欄位內容轉存為write.csv (需為UTF-8編碼格式)，
各欄位內容之間以一個半形逗號隔開。

提示：只需要輸出資料，不需要輸出欄位名稱。
"""
import json
import csv

with open('./read.json', 'r', encoding='utf-8')as f:
    # jsonfile = json.load(f)

    result = f.read()
    # print(result)
    jsonfile = json.loads(result)

    # print(jsonfile)

with open('./write.csv','a',encoding='utf-8',newline='')as c:
    csvfile = csv.writer(c)
    for j in jsonfile:
        csvfile.writerow([j['title'],j['showUnit'],j['startDate'],j['endDate']])
