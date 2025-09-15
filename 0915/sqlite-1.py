# 關聯式資料庫 RDBMS
# No SQL
import sqlite3

conn = sqlite3.connect('test.db')
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

conn.close()
# 主鍵

# https://sqliteviewer.app/