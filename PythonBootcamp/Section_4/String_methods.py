# STRING METHODS

# print(), len(), type(), sum(), max(), min(), round()
print(len('hsddbhc'))

print(dir(str))
help(str.replace)

s = 'Python'
new_s.upper()
print(s)
print(new_s)

print('prOgrammING'.lower())
s.capitalize()

# USEFUL STRING METHODS
my_str = 'I learn Python'

# 1. str.upper
print(my_str.upper())

# 2. str.lower()
print(my_str.lower())
# print(my_str)

# 3. str.strip()
ip = ' 192.254.0.1  '
ip = ip.strip()
print(ip)

value = '$$200$$$$'

# 4. str.replace()
new_value =value.replace('$', '%')

# 5. str.count()
txt = 'I learn this, thiS is not cool!'
n = txt.lower().count('this')
print(n)

print(txt.count('y'))

# 6. str,split()
my_list = txt.split()
print(my_list)

print('10.1..2.5.2'.split('.'))

# 7. str.join()
ip = '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = 'xxxxx'.join(ip_list)
print(ip_str)

# 8. str.find
my_str = 'I learn Python'
print(my_str.find('Pyxthon'))

# in
print('Golang' in my_str)

# not in
print('Golang' not in my_str)

print('$500 $600 $700'.count('$')

language = '$Python$$'
message = 'I love Python!'

# YOUR CODE STARTS HERE:
language1 = language.strip('$')  # remove all leading and trailing $ signs
language2 = language1.lower()  # lowercase version of language1 variable
message1 = message.upper()  # uppercase version of message variable
message2 = message.replace('Python', 'Java')  # replace Python with Java