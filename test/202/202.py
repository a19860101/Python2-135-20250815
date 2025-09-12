# 202

"""
請撰寫一程式，讀取新北市公共自行車即時資訊read.xml，
請將其中sno（站點代號）、sna（中文場站名稱）、tot（場站總停車格）
等三個欄位轉存為write.csv (需為UTF-8編碼格式)，
各欄位內容之間以一個半形逗號隔開。

提示：只需要輸出資料，不需要輸出欄位名稱。


輸出說明
將三個欄位的內容：sno、sna、tot，輸出至write.csv檔案，各欄位內容之間以一個半形逗號隔開
"""

import xml.etree.ElementTree as ET
import csv

tree = ET.parse('./read.xml')
root = tree.getroot()

with open('./write.csv','a',encoding='utf-8',newline='')as c:
    csvfile = csv.writer(c)

    for item in root.iter('row'):
        sno = item.find('sno').text
        sna = item.find('sna').text
        tot = item.find('tot').text

        csvfile.writerow([sno,sna,tot])
