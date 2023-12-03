import re
import requests


result = requests.get('https://ipap.ru')
text = result.text
print(text)

phones = re.findall(r'\d{7,11}', stroka)
print(phones)