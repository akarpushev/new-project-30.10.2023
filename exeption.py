#try:
    #print(a + b)
#except:
    #print('Произошла ошибка')

try:
    print(10 / 10)
except ZeroDivisionError:
    print('на 0 делить нельзя')
except NameError:
    print('переменная не задана')
except ValueError:
    print('невозможно привести к числу')
except TypeError:
    print('Ошибка типа данных')
except:
    print('Произошла ошибка!!!')

