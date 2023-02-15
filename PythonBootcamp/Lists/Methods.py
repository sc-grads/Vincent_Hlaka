# List Methods

# l1 = list()
# print(dir(l1))
# help(l1.append)

# adding to the list: append(), extend(), insert()
l1 = [1, 2.2, 'abc']
# 1.list.append()
l1.append(5)
# l1.append(6, 7) # this is an Error
l1.append([6, 7])
print(l1)

# 2. list.extend()
l1.extend('xy')
print(l1)

# 3. lis.insert()
years = [2020, 2022, 2023]
years.insert(1, 2021)
years.insert(len(years), 2024)
print(years)
# 4. list.clear
years.clear()
print(years)

# 5. list.pop
l2 = [10, 20, 30, 40]
x = l2.pop()
print(x)
print(l2)

y = l2.pop(1) # gives 20
print(y, l2)
l2.pop(100)

# list.remove()
l3 = [10, 20, 30, 40, 50, 60]
l3.remove(10)
print(l3)
while 20 in l3:
    l3.remove(20)
print(l3)


