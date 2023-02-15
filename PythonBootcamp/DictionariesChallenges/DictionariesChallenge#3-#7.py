# Challenge 3

# Considering the following dict, get a dict representation sorted by key.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
d1 = sorted(d1.keys())
print(d1)


# Challenge 4
# Considering the following dict, get a dict representation sorted by value.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
d1 = sorted(d1.values())
print(d1)


# Challenge 5

# generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).
# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.

employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
employees = sorted(employees.items())
print(employees)


# Challenge 6

# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.

employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
employees = sorted(employees.items(), key = lambda x:x[1][2],reverse=True)
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]


# Challenge 7

# Consider the dictionary called COUNTRY declared in this Python script.
# The keys are the country codes and the values are the country names.
# Print a sorted view of the dictionary, by the key (country code).
# NOTE the following
# keys = sorted(COUNTRY.keys())
#    print(keys)

# for k in keys:
#     print(f'{k} --> {COUNTRY[k]}')