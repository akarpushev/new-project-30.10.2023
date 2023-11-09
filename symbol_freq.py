#str_ = input()

f = open('old_man.txt','r')
for line in f:
    str_ = line.strip().join()
str_ = str(str_)
print(len(str_))

str_lower = str_.lower()
str_letters = "".join(c for c in str_lower if c.isalpha())
print(str_letters)
print(len(str_letters))
#list_ = list(str_)
#tuple_ = tuple(str_)

set_ = set(str_letters)
print(set_)
print(len(set_))

list_set_ = list(set_)
list_set_.sort()
print(list_set_)

i = 0

for i in range(len(list_set_)):

    #dict_.append(f'{i}:{list_set_[i] / len(str_letters)}')
    dict_ = {list_set_[i]: str_.count(list_set_[i]) / len(str_letters)}
    print(list_set_[i], str_.count(list_set_[i]) / len(str_letters))

print(dict_)

f.close()
#the_dict = {x:x*x for x in range(1,21)}
#dict.append(f'{a}:{a**2}')

#dct = {
	#'a': 1,
	#'b': 2
#}

#lst1 = ['c', 'd']
#lst2 = [3, 4]

#for i in range(0, 2):
	#key = lst1[i]
	#value = lst2[i]
	#dct[key] = value
#print(dct)




#print(str_)
#print(list_)
#print(tuple_)
#print(set_)
#print(length_set_)
#print(list_set_)

#print(str_.count(' '))  # Подсчет количества пробелов
