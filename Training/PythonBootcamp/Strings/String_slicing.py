# slicing

movie = 'The bug'
print(movie[0:2])

# string_variable[start:stop]

print(movie[2:5])
print(movie[:2])
print(movie[4:1])
print(movie[-2:])

# movie[:i] + movie[1:] is equal to movie
print(movie[:4] + movie[4:])
print(movie[:42])
print(movie[3:100])

print(movie[0:10:2])
print(movie[::])
print(movie[::-1])

print('Python 3!!!'[:7:2])
s[::-1][::-1] == s

# Exercise
my_str = 'eth0:192.168.122.1'

# using string slicing, define a variable called my_interface that stores the substring 'eth0'
my_interface = my_str[0:4]  # equivalent to:
# my_interface = my_str[:4]

digits = '0123456789'

##YOUR CODE STARTS HERE
#using string slicing, create a variable called x that stores the substring '9630'
x = digits[::-3]    # x is '9630'
