# Ex 33

# Create a variable called my_var that contains the second element of the list as a string ('2.3') concatenated to the first letter of the third element of the list which is 'a' and the last element of the tuple which is the last element of the list.

# my_var should store the string: 2.3ay

my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]
# code
my_var = str(my_list[1]) + my_list[2][0] + my_list[-1][-1]
print(my_var)  # => 2.3ay
