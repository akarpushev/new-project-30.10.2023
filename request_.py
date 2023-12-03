import requests
import re

result = requests.get('https://ipap.ru')
text = result.text
print(text)

phones = re.findall(r'\d{7,11}', stroka)
print(phones)