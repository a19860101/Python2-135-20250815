import sqlite3

conn = sqlite3.connect('test2.db')
cursor = conn.cursor()

sql_create_table = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INT,
    qty INT
)
'''
# cursor.execute(sql_create_table)
# 新增單筆資料
sql_insert = '''
INSERT INTO products (name, price, qty)VALUES(?,?,?)
'''

# for i in range(10):
#     cursor.execute(sql_insert,('拿鐵',80,10))

# cursor.execute(sql_insert,('拿鐵',80,10))

datas = [
    ('美式咖啡',60,10),
    ('卡布奇諾',150,2),
    ('焦糖瑪奇朵',220, 3)
]

# 新增多筆資料
# cursor.executemany(sql_insert, datas)

# name = input()
# price = input()
# qty = input()
# sql_insert_2 = f'INSERT INTO products (name, price, qty)VALUES({name},{price},{qty})'
# cursor.execute(sql_insert_2)

# 刪除資料
# sql_delete = 'DELETE FROM products WHERE id = 5'
# cursor.execute(sql_delete)

# sql_delete = 'DELETE FROM products WHERE id = ?'
# cursor.execute(sql_delete,'6')

# cursor.execute('DELETE FROM products WHERE id = 8')

# 更新資料
sql_update = 'UPDATE products SET name=?,price=?,qty=? WHERE id=?'
update_data = ('氣泡水',120,23,4)
cursor.execute(sql_update, update_data)



conn.commit()

conn.close()
