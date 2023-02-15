# Loops and Ranges

s = 0
for n in range(101): #range(0, 101, 1)
    s += n
print(f'sum: {s}')

for _ in range(10):
    print('Do something', _)

import random
names =['tim', 'paul', 'john', 'lol']
for _in range(3):
    print(f'choosing winner. round {_} ..')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('######')

