# Set methods

# Given
set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}


vset1 = {'a', 'b', 'c'}

# set3 contains all unique elements present in both set1 and set2
# union() or | returns the set of all unique elements present in all the sets.
# set3 = set1 | set2
set3 = set1.union(set2)

# set4 contains the common elements of set1 and set2
# intersection() or &  returns the set that contains the elements that exist in both sets
# set4 = set1 & set2
set4 = set1.intersection(set2)

# set5 contains the elements that exist only in set1, but not in set2
# difference() or - returns the set of elements that  exist only in set1, but not in set2.
# set5 = set1 - set2
set5 = set1.difference(set2)

# Removing 'c' from set1
set1.discard('c')
# remove the element 'c' from set1

# Frozensets are immutable sets
