# Ex 39

phone1 = ['1111', '2222', '2222', '1111']
phone2 = ['1111', '3333', '3333', '1111']

# Converting lists to sets (to remove duplicates) and using the union operation
# union() or | returns the set of all unique elements present in all the sets.
phone_numbers = set(phone1) | set(phone2)

# Equivalent to:
phone_numbers = set(phone1).union(set(phone2))

print(phone_numbers)  # => {'1111', '3333', '2222'}