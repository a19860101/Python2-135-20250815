import requests
import pandas as pd
import matplotlib.pyplot as plt

ns = []
for m in range(8):
    url = f'https://api.taiwanlottery.com/TLCAPIWeB/Lottery/Lotto649Result?period&month=2025-0{m+1}&pageNum=1&pageSize=50'

    res = requests.get(url, verify=False)

    jsonfile = res.json()
    # print(jsonfile['content']['lotto649Res'])
    lotto8 = jsonfile['content']['lotto649Res']

    for lt in lotto8:
        # print(lt['period'])
        # print(lt['lotteryDate'])
        # print(lt['drawNumberSize'])
        for n in lt['drawNumberSize']:
            # print(n)
            ns.append(n)

data = pd.Series(ns)
# print(ns)
print(data.value_counts())
# print(data.value_counts())

dataX = data.value_counts().keys()
dataY = data.value_counts().values

plt.bar(dataX,dataY)

plt.xticks(range(1,50))
plt.yticks(range(20))

plt.grid(axis='y')

plt.show()