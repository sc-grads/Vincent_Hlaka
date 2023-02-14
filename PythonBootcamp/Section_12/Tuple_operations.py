# tuple Operations

my_tuple = (1.4, 10, 'abc', True, (30, 40), 'x')
t1 = my_tuple + tuple('yz')
print(t1)

t2 = (1, 2, 'a') * 3
print(t2)
print(my_tuple[0:2])
print(my_tuple[:3])
print(my_tuple[2:])
print(my_tuple[::])
print(my_tuple[-1:0:-1])
movies = ('The gift', 'the lunch', 'casal')
for movie in movies:
    print(f'We are watching {movie}')
print('The lunch' in movies)
print('The lunch' not in movies)
