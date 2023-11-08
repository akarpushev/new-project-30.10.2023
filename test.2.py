f = open('user.txt', 'r')
#"insert into telsprav values('alexey','karpushev','m','89692442339')"
for line in f:

    line = line.strip().split(':')
    #split_line = line.split(':')

    name = line[0]
    surname = line[1]
    sex = line[2]
    phone = line[3]

    insert_string = f'"insert into telsprav values("{name}","{surname}","{sex}","{phone}")"'
    print(insert_string)


f.close()