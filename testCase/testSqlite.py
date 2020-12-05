# -*- codeing = utf-8 -*-
import sqlite3

# 获取连接
conn = sqlite3.connect("../sqlitedb/douban.sqlite")
# 获取游标
cursor = conn.cursor()
# 编写sql
sql = '''
    create table company(
        id int primary key not null,
        name text,
        address text,
        salary real
    )
'''
# 执行sql
cursor.execute(sql)
# 提交
conn.commit()
# 关闭连接
conn.close()
