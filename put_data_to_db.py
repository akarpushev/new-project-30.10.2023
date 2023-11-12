import pymysql
f = open('user.txt', 'r')
connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()

for line in f:
    line = line.strip().split(':')
    name = line[0]
    surname = line[1]
    sex = line[2]
    phone = line[3]
    cursor.execute(f'insert into telsprav values("{name}","{surname}","{sex}","{phone}")')

f.close()
connection.commit()


#cursor.execute("insert into telsprav values('alexey','karpushev','m','89692442339')")
#connection.commit()


