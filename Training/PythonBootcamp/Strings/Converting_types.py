# Converting types

# 1 mile = 1.609 km
miles =float(input('Enter distance in miles: '))
# print(type(miles))
# miles = float(miles)
km = miles * 1.609
print('Distance in km:', km)

a = 10
b = 2.5
c = '8.2'

# int => float
a_float = float(a)
print('a:', type(a))
print('a_float:', type(a_float))

# float => int
b_int = int(b)
print('b_int:', type(b_int))

# float => str
b_str = str(b)
print('b_str:', type(b_str))

# str => float
c_float = float(c)
print('c_float:', type(c_float))

# str => int
c_int = int(float(c))
print('c_int:', type(c_int))

str = 's'
a = 1
a_str = str(a)

print("He said: \\\"Pytho\n's beauty is simplicity.\"")
x = input('Enter x:')
y = input('Enter y:')
print(x * y)

x = int(input('Enter x:'))
print(x*2, type(x))

x = int(float(input('Enter x:')))
y = float(input('Enter y:'))
print(x + y)

str = 'Python'
version = 3
print(str + ' ' + str(3))

# exercises
# Consider the following variables: a = '1.5' and b = '2'
# Using Type Conversion create a new variable called c that stores the result of a multiplied by b.
# c is a float type and will be 3.0.
a = '1.5'
b = '2'
# Using Type Conversion create a new variable called c that stores the result of a multiplied by b. c stores a float and will be 3.0.
c = float(a) * float(b)
