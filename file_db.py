import sqlite3

# 指定数据库文件路径
db_file = "/home/vkeilo/.local/share/fsearch/fsearch.db"

# 连接到数据库文件
conn = sqlite3.connect(db_file)

# 创建一个游标对象，用于执行 SQL 查询
cursor = conn.cursor()

# 执行 SQL 查询，获取所有表格的名称
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# 获取查询结果
tables = cursor.fetchall()

# 打印表格列表
for table in tables:
    print(table[0])  # 表格名称位于元组的第一个元素

# 关闭游标和数据库连接
cursor.close()
conn.close()
