l1 = ['kirill', 'ivan', 'pavel', 'ivan']
l1.append('sergey')

l2 = ['anna', 'maria', 'ekaterina']
l1.append(l2)
print(l1)

l1.extend(l2)
l1.insert(1, 'alexander')
l1.remove('kirill')
l1.reverse()
l1.pop(3)
print(l1.index('ivan'))
print(l1.count('ivan'))

l3 = ['kapusta']
l4 = l3.copy()
l3.append('kartofel')


print(l1)
print(l3)
print(l4)
print(l1[2][1])