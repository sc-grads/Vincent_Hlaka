# Formatting strings (f-strings)

first_name = 'John'
last_name = 'Williams'
age = 40
print('Hello ' + first_name + ' ' + last_name + '! YOu are ' + str(age) + ' years old')
print(f'Hello {first_name} {last_name}! You are {age} years old.')

s = f'{2.3 * 4.2 / 5.1:.4f}'
print(s)

# converting fahrenheit = celsius * 1.8 + 32
celsius =15.4
print(f'{celsius} degrees Celsius = {celsius * 1.8 +32} degrees Fahrenheit.')

name = 'Maria'
age = 40
city = 'Bucharest'
print(f'My name is {name}, ' + f'I am {age} old ' + f'and I live in {city}.' )



