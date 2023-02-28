# Intro to lists

l1 = [1, 2.5, 'python', True, ['abc', 'xyz'], (10, 20, 30)]
print(len(l1))
l2 = []  # empty list
l3 = list()  # empty list
print(l1[0])
x = l1[-1]
print(x)
# print(l1[10])

# s1 = 'abc'
# s1[0] = 'X' # str is immutable
l4 = list('abcd')
print(l4)
print(id(l4))
l4[0] = 'X'
l4.append(100)
print(id(l4))

l1 = ['python', True, 'java1', 30]
l1[2] = 10
print(l1)
