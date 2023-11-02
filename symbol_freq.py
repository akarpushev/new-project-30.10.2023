str_ = input()

str_ = str(str_)
length_ = len(str_)
list_ = list(str_)
tuple_ = tuple(str_)
set_ = set(str_)
length_set_ = len(set_)
list_set_ = list(set_)
list_set_.sort()

i = 0
for i in range(length_set_):
    print(list_set_[i], str_.count(list_set_[i]) / length_)

#print(str_)
print(length_)
#print(list_)
#print(tuple_)
#print(set_)
print(length_set_)
print(list_set_)

print(str_.count(' '))  # Подсчет количества пробелов
