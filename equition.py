print('Программа для решения квадратных уравнений!')
bad_data = True #исходно данные плохие

while bad_data == True:
    try:
        a = int(input("Введите число а: "))
        b = int(input("Введите число b: "))
        c = int(input("Введите число c: "))
        bad_data = False
    except ValueError:
        print('данные не привести к числу')

#from rumath import koren
from math import sqrt as koren

D = b**2 - 4 * a * c
print('Дискриминант равен:', D)

if D > 0:
    d = koren(D)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    print(f'уравнение имеет два корня x1={x1}, x2={x2}')
    print('уравнение имеет два корня x1={}, x2={}'.format(x1,x2))

elif D == 0:
    x = -b / (2 * a)
    print(f'уравнение имеет 1 корень x={x}')
else:
    print('уравнение не имеет корней')

print(f'x1={x1}, x2={x2}')
print(f'x1={x1} \n x2={x2}')


