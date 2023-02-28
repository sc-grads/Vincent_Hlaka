# Ex 38

names1 = {'John', 'Marry', 'Lena', 'Pollux'}
names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}

# Set Intersection
names = names1 & names2  # names is of type set
names = list(names)  # converting set to list

print(names)  # => ['Lena', 'Marry']