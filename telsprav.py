import pymysql
import datetime
phone_cach = {}

while True:
    username = input('Введите имя абонента: ').capitalize()
    start_time = datetime.datetime.now()
    phone = phone_cach.get(username, None)
    if phone != None:
        print(f'Телефон абонента {username} - {phone}')
        print('из словаря')
    else:
        connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test',
                                     port=33306)
        cursor = connection.cursor()
        cursor.execute(f'Select name, phone from telsprav WHERE name = "{username}"')
        connection.close()
        data = cursor.fetchall()
        #print(data)
        if len(data) > 0:
            #print(data[0][0], data[0][1])
            #name = data[0][0]
            phone = data[0][1]
            print(f'Телефон абонента {username} - {phone}')
            print('из БД')
            phone_cach[username] = phone
        else:
            print(f'Телефон абонента {username} не найден')

    end_time = datetime.datetime.now()
    work_time = end_time - start_time
    print(work_time)
