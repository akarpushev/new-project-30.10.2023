import pymysql
connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()
cursor.execute('select * from telsprav')
data = cursor.fetchall()

users = []
for elem in data:
    name = elem[0]
    surname = elem[1]
    sex = elem[2]
    phone = elem[3]
    users += [(f'{name} {surname} {sex} {phone}').split()]
#print(users)

while True:
    username = input("Введите имя: ")
    for name in users:
        if name != username:
            print('Телефон абонента', username, users[3])

    print('Абонент', username, 'отсутствует')

