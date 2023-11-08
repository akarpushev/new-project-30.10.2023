import pymysql

connection = pymysql.connect(host='10.10.101.161', user='pyuser', password='123456', database='test')

cursor = connection.cursor()

cursor.execute("insert into telsprav values('alexey','karpushev','m','89692442339')")
connection.commit()

f = open('user.txt', 'r')
for line in f:
    line = line.strip().split(':')
    name = line[0]
    surname = line[1]
    sex = line[2]
    phone = line[3]
    insert_string = f'"insert into telsprav values("{name}","{surname}","{sex}","{phone}")"'

    cursor.execute(insert_string)
    connection.commit()
f.close()
