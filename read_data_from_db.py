import pymysql
connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()

cursor.execute('select * from telsprav')

data = cursor.fetchall()

for element in data:
    #print(element)
    name = element[0]
    surname = element[1]
    sex = element[2]
    phone = element[3]

    print(name, surname, sex, phone)