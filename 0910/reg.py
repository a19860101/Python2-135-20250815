# 正則表達式、正規表達式
# regular expression

import re

# 基本比對
s = 'hello python !! hello Hello Python'
# role = re.search('hello', s)
# role = re.search('hello', s)
# role = re.search('Hello123', s)
# role = re.findall('hello', s)
role = re.finditer('hello', s)
print(role)

for r in role:
    print(r)


#
s = 'Hello 123'

# role = re.compile(r'[a-z]')
# role = re.compile(r'[A-Z]')
# role = re.compile(r'[a-zA-Z]')
# role = re.compile(r'[0-9]')
# role = re.compile(r'[13]')
# role = re.compile(r'^[a-zA-Z]')
# role = re.compile(r'^[0-9]')
# role = re.compile(r'[0-9]$')
# role = re.compile(r'[a-z]$')
# role = re.compile(r'^[a-z]$')
# role = re.compile(r'^[a-zA-z]$')
role = re.compile(r'^[a-zA-z]+[0-9]+$')

result = role.search(s)

# print(result)

# 電話號碼

p = '02-1234-5678'
prole = re.compile(r'^02-[0-9]{4}-[0-9]{4}$')
presult = prole.search(p)
# print(presult)

# 手機
phone = '0912-345-675a'
# phone_role = re.compile(r'^[0-9]{4}-[0-9]{3}-[0-9]{3}$')
phone_role = re.compile(r'^\d{4}-\d{3}-\d{3}$')
phone_result_s = phone_role.search(phone)
phone_result_m = phone_role.match(phone)
print(phone_result_s)
print(phone_result_m)


# 身分證
r'^[A-Z][12][0-9]+$'
identity = 'a223456789'
id_role = re.compile(r'^[A-Z][12][0-9]{8}$')
id_result = id_role.search(identity)
# print(id_result)

