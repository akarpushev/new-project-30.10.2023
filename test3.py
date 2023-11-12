f = open('user.txt','r')
g = open('users2.txt', 'w')
for elem in f:
    elem = elem.strip().split(':')
    name = elem[0]
    surname = elem[1]
    sex = elem[2]
    phone = elem[3]
    user = f'{phone},{sex},{surname},{name}'
    user = user.replace(',', ';')
    g.write(user+'\n')
f.close()
g.close()