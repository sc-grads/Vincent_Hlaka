# String concatenation and repetition
# + => concatenation operator

movie = 'The Evil'
director = 'Don Peters'
movie_and_director = movie + director
print(movie_and_director)
print(movie + 'was directed by ' + director)

print('abc' '123')
# cannot + string with float
# lang = 'Python'
# version = 3.22
# print(lang + version) it will have an error
# solution
# print(lang + str(version))

# * => the repetition operator

print(movie * 5) # returns the values movie 5*

# Exercise
my_str = 'Python is TIOBE language of the year 2023!'

# define a variable named s1 that stores the character T from the string above. Use a positive index to get the character T
s1 = my_str[10]
print(s1)

# define a variable named s2 that stores the character 3 from the string above. Use a negative index the get the character 3
s2 = my_str[-2]
print(s2)

# concatenate s1 and s2 into a new variable called s3. s3 will store the string 'T3'
s3 = s1 + s2
print(s3)

a, b = '1', '2'
print(a + b * 3)