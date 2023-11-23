import re

stroka = 'Privet menya zovut Alexey, mne 48 let, moi telephon 89632442231, a pochta akarpushev@yandex.ru'

# result = re.match(r'Privet menya zovut', stroka)
# print(result)
# print(result.group(0))
# print(result.start())
# print(result.end())
#
# result = re.search(r'telephon', stroka)
# print(result)
# print(result.group(0))
#
# result = re.split(r'moi', stroka)
# print(result)
#
# result = re.findall(r'telephon', stroka)
# print(result)

#phones = re.findall(r'\d+', stroka)
#pohnes =re.findall(r'\b\d\d\d\d\d\d\\b', stroka)
phones = re.findall(r'\d{7,11}', stroka)
print(phones)
email = re.findall(r'\w+@\w+\w+', stroka)
print(email)