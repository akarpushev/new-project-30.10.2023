import pymysql
connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()
cursor.execute('select name, phone from telsprav')
data = cursor.fetchall()
connection.close()

users = {}
for elem in data:
    users[elem[0]] = elem[1]
print(users)

while True:
    username = input('Введите имя абонента: ').capitalize()
    phone = users.get(username, 'не найден')
    print(f'Телефон абонента {username} - {phone}')




    # for name, phone in users.items():
    #     if username == name:
    #         print('Телефон абонента', username, phone)
    #         break
    #
    #     print('Абонент', username, 'отсутствует')

