f = open('user.txt','r')

for line in f:
    #print(line)
    line = line.strip()
    split_line = line.split(':')
    #print(split_line)
    #print(split_line[0])
    name = split_line[0]
    surname = split_line[1]
    sex = split_line[2]
    phone = split_line[3]
    #print(f'Привет, меня зовут {name}, моя фамилия {surname}, мой пол {sex}, а телефон мой {phone}')

    insert_string = f'insert into telsprav values("{name}","{surname}","{sex}","{phone}")'
    print(insert_string)


f.close()