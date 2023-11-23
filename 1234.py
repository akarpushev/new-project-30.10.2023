
def get_user_data():
    a = input('VV a: ')
    b = input('VV b: ')
    try:
        a = int(a)
        b = int(b)
        return a, b
    except:
        a = None
        b = None
        return a, b



if __name__ == '__main__':
    oper = input('VV oper: ')
    a,b =get_user_data()
    if oper == 'plus' and a != None and b != None:
        c = a + b
        print(c)
    elif oper == 'minus' and a != None and b != None:
        c = a - b
        print(c)

