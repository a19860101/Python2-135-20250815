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
# 刪除欄位
sql_drop_column = '''
ALTER TABLE products DROP COLUMN qty
'''
# 新增欄位
sql_add_column = '''
ALTER TABLE products ADD COLUMN qty INT
'''
# 更改欄位名稱
sql_rename_column = '''
ALTER TABLE products RENAME name TO title
'''
# 更改資料表名稱
sql_rename_table = '''
ALTER TABLE qqq RENAME TO products

'''

cursor.execute(sql_rename_table)

conn.close()
# 主鍵

# https://sqliteviewer.app/