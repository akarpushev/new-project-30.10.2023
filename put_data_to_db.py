import pymysql

connection = pymysql.connect(host='10.10.101.161', user='pyuser', password='123456', database='test')

cursor = connection.cursor()

cursor.execute("insert into telsprav values('alexey','karpushev','m','89692442339')")
connection.commit()