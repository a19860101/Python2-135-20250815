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
cursor.execute(sql_create_table)

sql_insert = '''
INSERT INTO products (name, price, qty)VALUES(?,?,?)
'''

for i in range(10):
    cursor.execute(sql_insert,('拿鐵',80,10))

cursor.execute(sql_insert,('拿鐵',80,10))

# name = input()
# price = input()
# qty = input()
# sql_insert_2 = f'INSERT INTO products (name, price, qty)VALUES({name},{price},{qty})'
# cursor.execute(sql_insert_2)

conn.commit()

conn.close()
