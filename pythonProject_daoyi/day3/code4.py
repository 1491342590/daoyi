import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='pytest',
    port=3306
)

# 查询
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print(data)
# cursor.close()

# 创建表
# cursor = db.cursor()
# sql="""
# CREATE TABLE testtable(
#     id int not null,
#     sex char(20) not null
# )
# """
# cursor.execute(sql)
# cursor.close()

# 插入
# cursor = db.cursor()
# sql="""
# INSERT INTO testtable
#     (id,sex)
# values(1,'abc')
# """
# cursor.execute(sql)
# cursor.close()

# 查询
cursor = db.cursor()
sql="""
SELECT * FROM testtable
"""
cursor.execute(sql)
res = cursor.fetchall()
cursor.close()
for i in res:
    print(i[0],i[1])