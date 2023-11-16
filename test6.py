dict1 = {'kirill': 89112345544, 'ivan': 89112343321, 'oleg': 89765432132}
#try:
    #name = input('Введите имя: ')
    #print(f'Телефон {name}: {dict1[name]}')
#except KeyError;
    #print('Имени нет')
dict2 = {
    'fedor': 98234599988,
    'kirill': 1111111111
}
dict1.update(dict2)

dict1['viktor'] = 9998887765
print(dict1)


name = input('Введите имя: ').lower()
print(f'Телефон абонента {name} - {dict1.get(name,"не найден")}')
print(dict1.items())
print(dict1.values())
print(dict1.keys())

