vegetables = ('капуста', 'морковь', 'картофель', 'помидоры')
f = open('vegetables.txt', 'w')

for vegetable in vegetables:
    f.write(vegetable+'\n')

f.close()


