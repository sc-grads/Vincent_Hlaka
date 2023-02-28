# for, cont and pass statements

for letter in 'Go Python goooo!':
    if letter == 'o':
        continue
    print(letter, end='')

# even or odd

for n in range(10):
    if n % 2 == 0:
        print(f'Found an even: {n}')
        continue
    print(f'Fount an odd: {n}')

for _ in range(100):
    pass