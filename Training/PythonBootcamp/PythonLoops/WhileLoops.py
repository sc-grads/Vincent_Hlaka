# While loops

x = 0
while x < 10:
    print(f'The current value of x is {x}')
    x = x + 1  # same as x += 1
else:
    print(f'Finishing printing. x is now {x}')

print('after while')

# quiz
a = 5
if a < 5:
    for i in range(10):
        print(i , end=' ')
elif a > 5:
    for i in range(5):
        print(i , end=' ')
else:
    for i in range(7):
        print(i, end=' ')
for i in range (18, -4, -5):
    if i == 13: continue
    print(i, end=' ')