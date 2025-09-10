import csv

with open('test.csv','w',encoding='utf-8',newline='') as f:
    csvfile = csv.writer(f)
    # csvfile.writerow(['apple','banana','cat'])
    csvfile.writerows(
        [
            ['apple','banana','cat'],['apple', 'banana', 'cat']
        ]
    )


