# LIST GOTCHAS

l1 = [1, 2, 3]
l2 = l1
l1[0] = 'XX'
l2.append(10)
print(f'l2: {l2}')
print(f'l1: {l1}')
print(id(l1), id(l2))
l1.remove(2)
print(f'l2: {l2}')

l3 = l1.copy()
l3.append('abc')
print(f'l1: {l1}')
print(f'l3: {l3}')
# print(id(l1), id(l3)')

#2
# l1.extend(['x', 'y'])
# rint(l1)
# l1.append(20)
# l1.extend([20])

# my_list = [[1, 2], 1, 2.5, 'a', ['a', 'b', 3.3]]
# print(my_list[2:])


# l1 = [c.lower().upper() for c in 'aBc']
print(l1)






