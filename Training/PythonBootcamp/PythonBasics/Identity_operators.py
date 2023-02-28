# identity operators: "is" and "is not"

a, b = 3, 4
print(a is b)

# Immutable types: int, floats, str, tuple, frozenset
# Mutable types: list, set, dict

print(id(a))
a += 3
print(a)
print(id(a))

numbers = [1, 2, 3]
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers))

nums = numbers.copy()
print(nums == numbers)
print(nums is numbers)

a = 5
a **= 2
a /= 5
print(a)
print(round(10/3, 5))
a = 7
id1 = id(a)
a += 100
id2 = id(a)
print(id1 == id2)
l1 = [1, 2]
id1 = id(l1)
l1.append(100)
id2 = id(l1)
print(id1 == id2)
a, b, c, d = 2, 4, 6, 8
print(a > b, a >= b, a < c, d >=c, d == d, d !=- b)
