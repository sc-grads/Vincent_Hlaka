# Tuple Intro

t1 = tuple()
t2 = ()
print(print(t1), type(t2))
t3 = (1, 3.4, 'python', True)
print(t3)

t4 = (10,)

t5 = 6.9, True, 10, 'abc'
print(type(t5))

t6 = tuple([1, 2, 3, 4])
t7 = tuple('hello')
print(type(t6), type(t7))
l1 = list(t5)
print(l1)

print(t5[0])