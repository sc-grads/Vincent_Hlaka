# Concatenation

l1 = [3, 4]
print(l1, id(l1))
l1 =l1 + [5, 6]
print(l1, id(l1))

l1 += [7, 8]
print(l1, id(l1))

l1.extend([11, 12])
print(l1, id(l1))

# append vs extent
l1.append(['a', 'b'])
print(l1)
l1.extend(['x', 'y'])
print(l1)
l1.append(20)
l1.extend([20])
print(l1)
# l1.extend(20) this is an error

l2 = list('abc')
l3 = l2 * 3
print(l3)

# SLICING
print('#' * 10 + ' List slicing ' + '#' * 10)
numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'numbers: {numbers}')
print(numbers[:3])  # start is default zero
print(numbers[2:])  # stop is default the end of the list
print(numbers[1:5:3])
print(numbers[4:1:-2])
print(numbers[::])
print(numbers[::-1])
print(numbers[1:100])
numbers[0:2] = ['a', 'b']
print(numbers)
numbers[0:2] = ['x', 'y', 'z']
print(numbers)
print('#' * 10 + 'LIST ITERATION ' + '#' * 10)
ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
for ip in ip_list:
    print(f'connecting to {ip} ...')

print('10.0.0.1' in ip_list)  # True
print('192.100' in ip_list)  # False
print('192' in ip_list)  # True
