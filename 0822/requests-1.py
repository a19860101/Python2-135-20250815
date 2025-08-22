import requests
import bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# url ='https://www.mobile01.com/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'cookie': 'ak_bmsc=B5A5947859FBDD3DACAA085365FB5177~000000000000000000000000000000~YAAQehAuF1OO46aYAQAAjomOrRzbfB8xg1YFKtDNGHfsK38eXQkHtd5ByUyIjZsNO8B4cUMvAMPU2wTYtdyURyq8HO04AZMw3UWyPczs5/wnhYDO4vx0ajiV7X8irhY9QrjPcbkW2IdZCfCTbTyRytkoDKSkWCzaLI9g9faIcPmk0idG1DCG7MKQkmHmKngk0iSJfwjP216uWZgsJRF6B/EcxpQFj2gRxUjqMtxTh86CvkNsFEkywdaYfZ62q2j9zIrgrzrK2b09oeyB5WXMCwxd9tnLXfuBnfkCa+zkl3f3acpP45oxwfMd370osR/IQVfUOt25E4fX0N7Lyk8igHBpCk+T+LmW9ps8Jp6x7c+mx3wOFesVsFaCE9bZ0uGlrD8WJg9jQltg1mn0iRoG; _pubcid=5f6ba8e7-81e1-45f7-8af9-e437c828753f; _pubcid_cst=zix7LPQsHA%3D%3D; ucf_uid=a9dc6482-f19f-44b6-b665-ff0f406149d4; _gcl_au=1.1.1037964772.1755258458; _ga=GA1.1.2057596258.1755258458; __retuid=8cddb03-cfef-9f7b-5328-45fbe745ac02; __fpid=15901d719f2332cd6a6080a5ef67acf7; __gads=ID=6478f4243b73d5e7:T=1755258458:RT=1755258458:S=ALNI_MY79UsdLEcJ3FNyLPlhc2-azCc43A; __gpi=UID=000011809bc3abf9:T=1755258458:RT=1755258458:S=ALNI_MZ7HDbt5jotFarEbQzSKpO27g3qLw; __eoi=ID=76a2d47152704b0b:T=1755258458:RT=1755258458:S=AA-AfjY5d3NtNHyL2DKXQcvTQJu4; __htid=a26ebc22-b060-499f-b2e6-73ca2128f282; _ht_em=1; _ht_5aaa20=1; bm_sz=97D04939BEFF7D7138ED3FBCF14BAEFB~YAAQy4pFy5mAtaWYAQAAV1aPrRx7PtVSpXPWkjsq9hKiAX4huOPOgjr0uCxTh8WFOEk1aHckk46swAy44u9FFMiNqA43dRuKLS6tQpeMCkx5XCNVApWtjhRfyMlrYbWFzgROKXA87WoOWKLD3hdmhoaKh9WX8FSE75UMTIy8/nEz56E6ZltYkbnSzS7FOmOYsmwBjdLMHF329I44ZorLLYc9LQr8I9BOdUeQideNTPuhdtAWXoVjvzUENjSY0LPU+f7Si/ALnyAzE/hEsxjKctp9wGN4yOEM3h7SXVDkga6QnF6cb75EbYrhLxwu3It7ephlDTx4oXlQ19FVkeTEYNG0qq7nC/6eNl123Ulb5A+C/Axzo2lNDWTf481Y21AlykuDqA5KOcoBzmpntC/+22dupvOUOfp7CA1WH4Ty5w28~3425073~3552053; _abck=1CFE50955B1CAF9CCCC2ED25F93D1E6A~0~YAAQy4pFy+SAtaWYAQAAs1aPrQ46pVyS1dyl0j8DtJhVgzsjG69S2dR5jLf/vxH7SImzZXV6ZP46VQfdZvg0ly7L4WXpn3C9IxGUJAHWcjmbmUeoBHkIXXtPFOyDIn4Cbay4FL16VxLi26AnQ+Tw/Brc7Z8Dk1iKBh3mjPCPNM+3yJTLUwcuXg+6OI2xnXSTzLm3B/Zj318YOFcWIGDPZi56cU2K6tzvkzC92B71yoIzXDg6R4i1yvOxD51hJu3+OhM/L+AyWaijhXZCpJKQqa9LRyaH6dCQ7KCwgB7APMDyygEiGa5a2YQYJW8dX6/lZHkbkfzYotg5EIRxsKZy6SD/dNEfehaJKFBhQJ1em7aF5+EPnV896glMQyrwZuQoRKEPEQ1JmWEViJe0/X1AeEC8DekraN01jq6i0Nd8nlFHSUSQTdKkDNnRzuz9Tn0JXx2Pg4CjzCgP5z0iuhkXjHhSxxs3j9UxBodEJLNFPByaap4JdZuAcVsZS6zvt6y1U9le1fqQq5j/9lvLJQ533kLuunW/LYJkCPAZkam8+94nyfyRaeE0F12CzHuFPFzfWW4G4l9n5GusqBPOf7tD0Zcijf4Dz6EXaLM5OO7gZYH390XhmQqDqB5VRS7NS6iiW7xWR77ElGWDzxKZB3TJiF1JJeGczsww1bjykA==~-1~-1~-1; _tfpvi=ZTRjYWI3ZGItMDVkZC00M2VlLTllNDAtNWMzNWE4Njk4N2M2Iy04LTg%3D; bm_sv=39CDF0CC224C67FA68C2054EB0AE4C10~YAAQy4pFy2uDtaWYAQAAPlqPrRzAn3BwiyhPO1R1EOpSotZzrLNdMaXMmg1dn0IB13omf3K7Xiq+Gb4yX34WPg7VrkZD3TTrydwnTRqrFC44ExlvI95/BsdoxfjdI0AOQs0dmVCESYN7jcibHL8Q3dZP9B/m4Y8C7z4PXfiQDa3bCgvVnCBDJHDBYfZUfQXVTwI7YpU4BAF39Sam1yBWUW7HcuCa4G7UwpHMo4u5Ykby0oPpvy3WhQRjK++MniykV6c=~1; cto_bundle=sFnvil9kZVo1ekJpd21SUWZ4TVRsMVVDOWZ5UkY1UkJjT3BQMWY0Rk8lMkZ2N0VFamZCeDhtWWxtVVo4eFZURjZLYnVWNFNMJTJCU3BDJTJCcGNwTDJBYU9KMzY5JTJGYTk1MHA2NUk5WmJqSlViOVlCMURidkN2Z05FV01WbXMlMkZ6TUJNWElycGlnZ1M; cto_bidid=UDGXTl9lUEtQMFpYV3JIOUpCdVA1cUpSVFJYJTJGZ3lJelFjMW1VdnQlMkY1cWxhcFZzaU9PQXVWZVBjWTZZWXZUQVNMYVZiVjY0OThRdnluSXluTyUyRldVMWg1VWx1QSUzRCUzRA; __retfs=fSes-63d3bff3-ef0d-fc28-db03; _ht_hi=1; nineyi_did=519c5a3f-8b40-4192-bd66-88f40e4cc2df; _ga_2MYKFYXMP7=GS2.1.s1755258458$o1$g1$t1755258510$j9$l0$h0; _ga_952J398MTY=GS2.1.s1755258458$o1$g1$t1755258510$j9$l0$h0; _ga_DCHTH48ZN2=GS2.1.s1755258458$o1$g1$t1755258510$j8$l0$h0; FCNEC=%5B%5B%22AKsRol_xGG04gNopd9K2d8smYFPk9gz1Y1yzF1MdCEAItBSOCPLue3ziTNDbUB0nRuXSlQJsbj4VY4YGgP4g-deur43JlWaMWMjlcGaii1t_sBqbOC-XzyxyKuoZR6lDiGis-Nk6eSDUJt1nGAsjJ8YswbC20NvmUQ%3D%3D%22%5D%5D',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9',
}

res = requests.get(url, headers=header, verify=False)

print(res.text)
result = res.text

html = bs4.BeautifulSoup(result, 'html.parser')

# print(html)

data = html.find_all('div',class_='r-ent')
for item in data:
    # print(item.find('div',class_='title').text)
    title = item.find('div',class_='title').a.text
    date = item.find('div',class_='date').text
    author = item.find('div',class_='author').text
    nrec = ''
    if item.find('div',class_='nrec').span is not None:
        nrec = item.find('div',class_='nrec').span.text
    else:
        nrec = '0'

    print(title,date,author, nrec)
